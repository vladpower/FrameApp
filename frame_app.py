import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import design  # Это наш конвертированный файл дизайна
from frame import Slot, Frame

class FrameApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self._scheme = Frame.load_from_db()
        self.getAll_pb.clicked.connect(self.get_all)
        self.frame_tw.itemSelectionChanged.connect(self.print_slots)
    
    def get_all(self):
        main_item = QtWidgets.QTreeWidgetItem([self._scheme._name_])
        frames = [self._scheme]
        frame_items = [main_item]
        self._frames = {}
        while(frames):
            frame = frames.pop(0)
            item = frame_items.pop(0)
            for child in frame._children_.values():
                new_item = QtWidgets.QTreeWidgetItem([child._name_])
                item.addChild(new_item)
                frames.append(child)
                frame_items.append(new_item)
                self._frames[new_item.text(0)] = child
        self.frame_tw.clear()
        self.frame_tw.addTopLevelItem(main_item)

    def print_slots(self):
        frame_item = self.frame_tw.selectedItems()[0]
        if frame_item.text(0) in self._frames:
            frame = self._frames[frame_item.text(0)]
            self.slot_tw.clear()
            self.slot_tw.setRowCount(0)
            i=0
            for slot in frame._slots_.values():
                self.slot_tw.setRowCount(i+1)
                new_slot = QtWidgets.QTableWidgetItem(slot._name)
                new_slot.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
                self.slot_tw.setItem(i, 0, new_slot)
                new_item = QtWidgets.QTableWidgetItem(str(slot._value))
                new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)
                self.slot_tw.setItem(i, 1, QtWidgets.QTableWidgetItem(new_item))
                i+=1



        
        

