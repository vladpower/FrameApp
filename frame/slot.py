__all__ = ('Slot',)


class Slot:
    """
    Слот
    """
    # Имена системных слотов
    SYSTEMS_NAMES = ('procedure')

    # -*- Указатели наследования -*-
    # Значение слота наследуется
    IT_SAME = 'SAME'
    # Значение слота не наследуется
    IT_UNIQUE = 'UNIQUE'
    # При отсутствии значения в текущем слоте оно наследуется из фрейма верхнего уровня,
    # однако в случае определения значения текущего слота оно может быть уникальным
    IT_OVERRIDE = 'OVERRIDE'

    def __init__(self, name, value, inheritance_type, daemon=None):
        self._name = name
        self._type = value.__class__.__name__
        self._inheritance_type = inheritance_type
        self._value = value
        self._daemon = daemon or (lambda: None)

    def __getattr__(self, attr):
        return getattr(self._value, attr)

    def __iter__(self):
        return iter(self._value)

    @property
    def is_system(self):
        return self._name in self.SYSTEMS_NAMES

    @property
    def inheritance_type(self):
        return self._inheritance_type

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        # FIXME: TypeError: Object of type 'function' is not JSON serializable
        return self._value# or self._daemon

    # noinspection PyCallingNonCallable
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def type(self):
        return self._type

    def print(self, depth):
        if not self.is_system and self._value!=None:
            print(" "*depth + self.name + ": " + str(self._value))