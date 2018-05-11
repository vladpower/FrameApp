from copy import deepcopy

from .slot import Slot

from .slot_types import FramePtrList

import json
import ast

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
        self.collect_slots()

    def collect_slots(self):
        """
        Агрегация слотов от своих предков
        """
        if(self._parent):
            for element in self._parent._slots_.values():
                if(element.name in self._slots_):
                    if(element.inheritance_type==Slot.IT_SAME \
                       or self._slots_[element.name].inheritance_type==Slot.IT_FINAL \
                       or element.inheritance_type==Slot.IT_OVERRIDE \
                       and self._slots_[element.name]==None):
                        self._slots_[element.name].value = element.value
                elif(element.inheritance_type in {Slot.IT_SAME, Slot.IT_OVERRIDE}):
                    slot = Slot(element.name, element.value, Slot.IT_FINAL)
                    self._slots_[element.name] = slot

    def find(self, req, slot_name='name'):
        if slot_name in self._slots_ and req==self._slots_[slot_name]._value or slot_name=='name' and req==self._name_:
            return self
        else:
            for child in self._children_.values():
                ret = child.find(str(req), slot_name)
                if ret != None:
                    return ret
        return None

    def find_list(self, req, slot_name='name'):
        list=[]
        if slot_name in self._slots_ and req==self._slots_[slot_name]._value or slot_name=='name' and req==self._name_:
            list.append(self)
        for child in self._children_.values():
            list.extend(child.find_list(str(req), slot_name))
        return list

    @staticmethod
    def _get_slot_args(name, params):
        if name in Slot.SYSTEMS_NAMES:
            return name, params.value, params.inheritance_type
        return params.name, params.value, params.inheritance_type

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
            if(slot.inheritance_type != Slot.IT_FINAL):
                slot_data = {
                    'name': slot.name,
                    'type': slot.inheritance_type,
                    'value': slot.value
                }
                if(slot.has_daemon):
                    slot_data['daemon'] = slot.daemon
                data['slots'].append( slot_data )
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
    def load_frame(data, parent=None): 
        frame = Frame(parent, data['name'])
        for element in data['slots']:
            slot_name = element.pop('name')
            slot_type = element.pop('type')
            slot_value = element.pop('value')
            if('daemon' in element):
                slot_daemon = element.pop('daemon')
            else:
                slot_daemon = None
            if(slot_name in frame._slots_):
                if(parent._slots_[slot_name].type == Slot.IT_OVERRIDE and slot_value):
                    frame._slots_[slot_name].value = slot_value
                    frame._slots_[slot_name].inheritance_type = slot_type
                    frame._slots_[slot_name].daemon = slot_daemon
            else:
                slot = Slot(slot_name, slot_value, slot_type, slot_daemon)
                frame._slots_[slot_name] = slot
                         
            
        if "children" in data:
            for element in data['children']:
                child = Frame.load_frame(element, frame)
                frame._children_[child.name] = child
        return frame

    def add_children(self, *children):
        """
        Добавить алгоритмы
        :type algorithms: tuple[el_scheme.algorithm]
        """
        for child in children:
            self._children_[child.name] = child

    def remove(self):
        """
        Удалить алгоритмы
        :type algorithms: tuple[el_scheme.algorithm]
        """
        if(self._parent and self.name in self._parent._children_):
            del self._parent._children_[self.name]
        self._children_.clear()


    @classmethod
    def load_from_db(self):
        """
        Загрузка фреймовой модели из базы данных (файл формата JSON)
        :return Объект типа Frame
        """

        file_path = settings.DB_FILE_PATH

        with open(file_path, 'r') as infile:
            data = json.load(infile)
        scheme = Frame.load_frame(data)
        print('Схема "{}" загружена из {}\n'.format(scheme, file_path))

        return scheme

    def save_to_db(self):
        """
        Сохранение в базу данных (файл формата JSON)
        """
        data = self.serialize()
        file_path = settings.DB_FILE_PATH

        with open(file_path, 'w') as outfile:
            json.dump(data, outfile, indent=2)

        print('Схема "{}" сохранена в {}\n'.format(self, file_path))