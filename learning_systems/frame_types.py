from frame import Frame, Slot, FramePtrList, Integer, Real, Text, Bool, Table


__all__ = (
    'Task','Algorithm'
)



class Task(Frame):
    """
    Задача обучения
    """

    def __init__(self, parent=None, name=None, **slot_values):
        super().__init__(parent, name, **slot_values)
        self._slots_.update( {
            'Алгоритмы':         Slot('Алгоритмы', [], Slot.IT_UNIQUE, "set_algs")
        } )


class Algorithm(Frame):
    """
    Алгоритм обучения
    """

    def __init__(self, parent=None, name=None, **slot_values):
        super().__init__(parent, name, **slot_values)
        self._slots_.update( {
            'Точность':      Slot('Точность', "", Slot.IT_UNIQUE),
            'Время обучения': Slot('Время обучения', "", Slot.IT_UNIQUE),
            'Линейность':     Slot('Линейность', "", Slot.IT_UNIQUE),
            'Параметры':    Slot('Параметры', "", Slot.IT_UNIQUE),
            'Примечание':         Slot('Примечание', "", Slot.IT_UNIQUE),
        } )