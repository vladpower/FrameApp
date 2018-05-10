from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from frame import Slot, Frame
class Procedures:
    
    @staticmethod
    def algs_to_child(scheme, frame, item):
        if('Алгоритмы' in frame._slots_ and frame._slots_['Алгоритмы'].value):
            for child_name in frame._slots_['Алгоритмы'].value:
                child = scheme.find(child_name)
                new_item = QtWidgets.QTreeWidgetItem([child._name_])
                item.addChild(new_item)

    @staticmethod
    def attach(scheme, frame, item):
        if('procedure' in frame._slots_):
            method = _attached[frame._slots_['procedure'].value]
            method(scheme, frame, item)

_attached = {'algs_to_child': Procedures.algs_to_child}         