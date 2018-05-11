from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from frame import Slot, Frame
from learning_systems import Task, Algorithm, dialog_set_algs

class AlgSetter(QtWidgets.QMainWindow, dialog_set_algs.Ui_dialogAlgs):
    def __init__(self, frame_app, frame, slot):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.main_window = frame_app
        self.frame = frame
        self.slot = slot
        frame_app.setEnabled(False)
        self.model = QtGui.QStandardItemModel(self.algs_lv)
        items = {}
        for alg in frame_app.get_algorithms().values():
            item = QtGui.QStandardItem()
            item.setText(alg.name)
            item.setCheckable(True)
            items[alg.name] = item
            self.model.appendRow(item)
        for alg_name in slot.value:
            if alg_name in items:
                items[alg_name].setCheckState(QtCore.Qt.Checked)
            
        self.algs_lv.setModel(self.model)

    def quit(self):
        self.main_window.setEnabled(True)
        self.close()

    def accept(self):
        print("accept")
        checked = []
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            if(item.checkState()):
                checked.append(item.text())
            
        self.slot.value = checked
        self.main_window._scheme.save_to_db()
        self.main_window.print_slots()
        if(self.main_window.frame_tw.selectedItems()):
            item = self.main_window.frame_tw.selectedItems()[0]
            for i in reversed(range(item.childCount())):
                item.removeChild(item.child(i))
            self.main_window.show_frame(self.frame, item)
        self.quit()

    def reject(self):
        print("reject")
        self.quit()