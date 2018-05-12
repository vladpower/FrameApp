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
        self.slot_tw.itemDoubleClicked.connect(self.upd_slot)
        self.addAlg_pb.clicked.connect(self.add_frame)
        self.applySlot_pb.clicked.connect(self.edit_slot)
        self.remove_pb.clicked.connect(self.remove_frame)
        self.searchName_pb.clicked.connect(self.search_name)
        self.searchSlot_pb.clicked.connect(self.search_slot)
        self._frames = {}

    def get_algorithms(self):
        return self._algorithms._children_

    def get_tasks(self):
        return self._tasks._children_
    
    def get_all(self):
        main_item = QtWidgets.QTreeWidgetItem([self._scheme._name_])
        self.show_frame(self._scheme, main_item)
        self.frame_tw.clear()
        self.frame_tw.addTopLevelItem(main_item)

    def show_frame(self, frame, item):
        self._frames[item.text(0)] = frame
        Procedures.attach(self._scheme, frame, item)
        for child in frame._children_.values():
            new_item = QtWidgets.QTreeWidgetItem([child._name_])
            item.addChild(new_item)
            self.show_frame(child, new_item)

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
                    if(slot.has_daemon):
                        new_item.setFlags( QtCore.Qt.ItemIsSelectable |  QtCore.Qt.ItemIsEnabled )
                    else:
                        new_item.setFlags( QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled )
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
                parent_item = self.frame_tw.findItems(alg_string, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
            elif(self.task_rb.isChecked()):
                frame = Task(self._tasks, name)
                self._tasks.add_children(frame)
                parent_item = self.frame_tw.findItems(task_string, QtCore.Qt.MatchExactly | QtCore.Qt.MatchRecursive)
            else:
                return
            if(parent_item):
                new_item = QtWidgets.QTreeWidgetItem([frame.name])
                parent_item[0].addChild(new_item)
                self._frames[name] = frame
            self._scheme.save_to_db()

    def upd_slot(self, item):
        if(item.column()==1):
            slot_name = self.slot_tw.item(item.row(), 0).text()
            if(self.frame_tw.selectedItems()):
                frame_item = self.frame_tw.selectedItems()[0]
                if frame_item.text(0) in self._frames:
                    frame = self._frames[frame_item.text(0)]
                    slot = frame._slots_[slot_name]
                    if(slot.has_daemon):
                        method = Procedures.get_daemon(slot.daemon)
                        if(method):
                            method(self, frame, slot)

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
                        slot = frame._slots_[slot_name]
                        if(not slot.has_daemon):
                            slot.value = value
                            self.update_children(frame)
        self._scheme.save_to_db()

    def update_children(self, frame):
        frame.collect_slots()
        for child in frame._children_.values():
            self.update_children(child)

    def remove_frame(self):
        if(self.frame_tw.selectedItems()):
            frame_item = self.frame_tw.selectedItems()[0]
            if frame_item.text(0) in self._frames:
                frame = self._frames[frame_item.text(0)]
                frame.remove()
                root = self.frame_tw.invisibleRootItem()
                (frame_item.parent() or root).removeChild(frame_item)
        self._scheme.save_to_db()

    def search_name(self):
        name = self.nameSearch_le.text()
        name = name[0].upper() + name[1:]
        frame = self._scheme.find(name)
        self.frame_tw.clear()
        self.show_result(frame)
        
    def search_slot(self):
        slot_name = self.slotName_le.text().lower()
        slot_name = slot_name[0].upper() + slot_name[1:]
        slot_value = self.slotValue_le.text().lower()
        res = self._scheme.find_list(slot_value, slot_name)
        self.frame_tw.clear()
        for frame in res:
            self.show_result(frame)

    def show_result(self, frame):
        if(frame):
            item = QtWidgets.QTreeWidgetItem([frame.name])
            self.show_frame(frame, item)
            self.frame_tw.addTopLevelItem(item)

       



        
        

