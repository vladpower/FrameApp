from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from frame import Slot, Frame
from learning_systems.alg_setter import AlgSetter


class Procedures:
    @staticmethod
    def algs_to_children(scheme, frame, item):
        if('Алгоритмы' in frame._slots_ and frame._slots_['Алгоритмы'].value):
            for child_name in frame._slots_['Алгоритмы'].value:
                child = scheme.find(child_name)
                if(child):
                    new_item = QtWidgets.QTreeWidgetItem([child._name_])
                    item.addChild(new_item)

    _dialog = None

    @staticmethod
    def set_algs(frame_app, frame, slot):
        Procedures._dialog = AlgSetter(frame_app, frame, slot)
        Procedures._dialog.show()


    @staticmethod
    def attach(scheme, frame, item):
        if('procedure' in frame._slots_ and frame._slots_['procedure'].value in _attached):
            method = _attached[frame._slots_['procedure'].value]
            method(scheme, frame, item)

    @staticmethod
    def get_daemon(daemon_name):
        if(daemon_name in _daemons):
            return _daemons[daemon_name]
        return None

_attached = {'algs_to_children': Procedures.algs_to_children}
_daemons = {'set_algs': Procedures.set_algs}
