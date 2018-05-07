from copy import deepcopy

from .slot import Slot

from .slot_types import FramePtrList

import json

import settings


__all__ = ('Frame',)


class Frame:
    """
    Фрейм
    """
    # _name_ = 'Фрейм'
    # _slots_ = []
    # _children_ = FramePtrList()

    def __repr__(self):
        return '<{}>'.format(self._name_)

    def __init__(self, parent=None, name=None, **slot_values):
        self._name_  = name
        self._slots_ = {}
        self._children_ = {}
        self._parent = parent

        #self._collect_slots()
        #self._set_slots_for_instance(**slot_values)

    def _collect_slots(self):
        """
        Агрегация слотов от своих предков
        """
        self.__slots = deepcopy(self._slots_)

        parents = self.__class__.__mro__
        for parent in reversed(parents):
            if parent not in (self.__class__, object, type):
                self.__slots.update(parent._slots_)
                for slot_attr, params in parent._slots_.items():
                    if not params:
                        continue
                    name, value, inheritance_type = self._get_slot_args(slot_attr, params)

                    if inheritance_type == Slot.IT_UNIQUE:
                        self.__slots[slot_attr] = (
                            (value.__class__(), inheritance_type)
                            if name in Slot.SYSTEMS_NAMES else
                            (name, value.__class__(), inheritance_type)
                        )

    def _set_slots_for_instance(self, **slot_values):
        """
        Инициализация слотов у конечного объекта
        """
        for attr_name, params in self.__slots.items():
            if params is None:
                continue
            slot = Slot(*self._get_slot_args(attr_name, params))

            if slot.inheritance_type != Slot.IT_SAME and attr_name in slot_values:
                slot.value = slot_values[attr_name]

            setattr(self, attr_name, slot)

    def find(self, req, slot_name='symbol'):
        if slot_name in self._slots_ and req==self._slots_[slot_name]._value or slot_name=='name' and req==self._name_:
            return self
        else:
            for child in self._children_.values():
                ret = child.find(str(req), slot_name)
                if ret != None:
                    return ret
        return None

    @staticmethod
    def _get_slot_args(name, params):
        if name in Slot.SYSTEMS_NAMES:
            return name, params[0], params[1]
        return params[0], params[1], params[2]

    @property
    def name(self):
        return self._name_

    def serialize(self):
        data = {
            attr: getattr(self, attr).value
            for attr in dir(self)
            if isinstance(getattr(self, attr), Slot) and (attr not in Slot.SYSTEMS_NAMES)
        }
        data['name'] = self._name_
        data['slots'] = []
        for slot in self._slots_.values():
            data['slots'].append( {
                'name': slot._name,
                'type': slot._type,
                'value': slot._value
            } )
        data['children'] = []
        for child in self._children_.values():
            data['children'].append( child.serialize() )
        return data

    @classmethod
    def deserialize(cls, data):
        """
        :type data: dict
        """
        frame = Frame(cls)

        for key, value in data.items():
            getattr(frame, key).value = value

        return frame

    @staticmethod
    def load_frame(cls, data): 
        frame = Frame(cls)
        frame._name_ = data['name']
        for element in data['slots']:
            slot_name = element.pop('name')
            slot_type = element.pop('type')
            slot_value = element.pop('value')
            slot = Slot(slot_name, slot_value, slot_type)
            frame._slots_[slot_name] = slot
        if "children" in data:
            for element in data['children']:
                child = Frame.load_frame(frame, element)
                frame._children_[child._slots_['symbol']] = child
        return frame

            
    @classmethod
    def load_from_db(cls):
        """
        Загрузка схемы из базы данных (файл формата JSON)
        :return Объект типа Scheme
        """

        file_path = settings.DB_FILE_PATH

        with open(file_path, 'r') as infile:
            data = json.load(infile)
        scheme = Frame.load_frame(cls, data)
        print('Схема "{}" загружена из {}\n'.format(scheme, file_path))

        return scheme

    def print(self, depth=0, left=10):
        """
        Вывести на экран содержимое
        """
        if(left>0):
            print(" "*depth + "<"+self._name_+">")
            for slot in self._slots_.values():
                slot.print(depth+2)
            for child in self._children_.values():
                child.print(depth+4, left-1)

    def add_children(self, *children):
        """
        Добавить алгоритмы
        :type algorithms: tuple[el_scheme.algorithm]
        """
        for child in children:
            if "symbol" in child._slots_:
                self._children_[child._slots_['symbol']] = child

    def remove(self):
        """
        Удалить алгоритмы
        :type algorithms: tuple[el_scheme.algorithm]
        """
        if(self._parent):
            del self._parent._children_[self._slots_['symbol']]
        self._children_.clear()

    def save_to_db(self):
        """
        Сохранение в базу данных (файл формата JSON)
        """
        data = self.serialize()
        file_path = settings.DB_FILE_PATH

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print('Схема "{}" сохранена в {}\n'.format(self, file_path))

