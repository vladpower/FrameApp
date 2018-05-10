from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import design  # Это наш конвертированный файл дизайна
from frame import Slot, Frame
from learning_systems import Task, Algorithm, Procedures

scheme_string = 'Обучающиеся системы'
alg_string = 'Алгоритмы'
task_string = 'Задачи'

# Имена системных слотов
NONDELETE_FRAMES = (scheme_string, alg_string, task_string)

class FrameApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self._scheme = Frame.load_from_db()
        self._algorithms = self._scheme._children_[alg_string]
        self._tasks = self._scheme._children_[task_string]
        self.getAll_pb.clicked.connect(self.get_all)
        self.frame_tw.itemSelectionChanged.connect(self.print_slots)
        self.addAlg_pb.clicked.connect(self.add_frame)
        self.applySlot_pb.clicked.connect(self.edit_slot)
        self.remove_pb.clicked.connect(self.remove_frame)
    
    def get_all(self):
        main_item = QtWidgets.QTreeWidgetItem([self._scheme._name_])
        frames = [self._scheme]
        frame_items = [main_item]
        self._frames = {}
        while(frames):
            frame = frames.pop(0)
            item = frame_items.pop(0)
            Procedures.attach(self._scheme, frame, item)
            for child in frame._children_.values():
                new_item = QtWidgets.QTreeWidgetItem([child._name_])
                item.addChild(new_item)
                frames.append(child)
                frame_items.append(new_item)
                self._frames[new_item.text(0)] = child
        self.frame_tw.clear()
        self.frame_tw.addTopLevelItem(main_item)

    def show_frame(self, frame, item):
        Procedures.attach(self._scheme, frame, item)
        for child in frame._children_.values():
            new_item = QtWidgets.QTreeWidgetItem([child._name_])
            item.addChild(new_item)
        

    def print_slots(self):
        if(self.frame_tw.selectedItems()):
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
                    header = self.slot_tw.horizontalHeader()       
                    header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
                    header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                    i+=1

    def add_frame(self):
        name = self.nameAlg_le.text()
        if(not self._scheme.find(name)):
            frame = {}
            if(self.alg_rb.isChecked()):
                frame = Algorithm(self._algorithms, name)
                self._algorithms.add_children(frame)
                parent_item = QtWidgets.QTreeWidgetItem([alg_string])
            elif(self.task_rb.isChecked()):
                frame = Task(self._tasks, name)
                self._tasks.add_children(frame)
                parent_item = QtWidgets.QTreeWidgetItem([task_string])
            else:
                return
            new_item = QtWidgets.QTreeWidgetItem([frame.name])
            parent_item.addChild(new_item)
            self._scheme.save_to_db()

    def edit_slot(self):
        for row in range(self.slot_tw.rowCount()):
            item = self.slot_tw.item(row,1)
            if(item):
                value = item.text()
                slot_name = self.slot_tw.item(row, 0).text()
                if(self.frame_tw.selectedItems()):
                    frame_item = self.frame_tw.selectedItems()[0]
                    if frame_item.text(0) in self._frames:
                        frame = self._frames[frame_item.text(0)]
                        frame._slots_[slot_name].value = value
        self._scheme.save_to_db()

    def remove_frame(self):
        if(self.frame_tw.selectedItems()):
            frame_item = self.frame_tw.selectedItems()[0]
            if frame_item.text(0) in self._frames:
                frame = self._frames[frame_item.text(0)]
                frame.remove()

       



        
        

