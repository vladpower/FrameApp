# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 624)
        MainWindow.setMinimumSize(QtCore.QSize(660, 620))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_tw = QtWidgets.QTreeWidget(self.groupBox_5)
        self.frame_tw.setObjectName("frame_tw")
        self.frame_tw.header().setVisible(False)
        self.verticalLayout_11.addWidget(self.frame_tw)
        self.horizontalLayout_6.addLayout(self.verticalLayout_11)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_7.sizePolicy().hasHeightForWidth())
        self.groupBox_7.setSizePolicy(sizePolicy)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.alg_rb = QtWidgets.QRadioButton(self.groupBox_7)
        self.alg_rb.setObjectName("alg_rb")
        self.horizontalLayout_4.addWidget(self.alg_rb)
        self.task_rb = QtWidgets.QRadioButton(self.groupBox_7)
        self.task_rb.setObjectName("task_rb")
        self.horizontalLayout_4.addWidget(self.task_rb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.nameAlg_le = QtWidgets.QLineEdit(self.groupBox_7)
        self.nameAlg_le.setObjectName("nameAlg_le")
        self.horizontalLayout_5.addWidget(self.nameAlg_le)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.addAlg_pb = QtWidgets.QPushButton(self.groupBox_7)
        self.addAlg_pb.setObjectName("addAlg_pb")
        self.verticalLayout_2.addWidget(self.addAlg_pb)
        self.remove_pb = QtWidgets.QPushButton(self.groupBox_7)
        self.remove_pb.setObjectName("remove_pb")
        self.verticalLayout_2.addWidget(self.remove_pb)
        self.getAll_pb = QtWidgets.QPushButton(self.groupBox_7)
        self.getAll_pb.setObjectName("getAll_pb")
        self.verticalLayout_2.addWidget(self.getAll_pb)
        self.verticalLayout_13.addWidget(self.groupBox_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_13)
        self.verticalLayout_5.addWidget(self.groupBox_5)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.slot_tw = QtWidgets.QTableWidget(self.groupBox_6)
        self.slot_tw.setLineWidth(1)
        self.slot_tw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.slot_tw.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.slot_tw.setObjectName("slot_tw")
        self.slot_tw.setColumnCount(2)
        self.slot_tw.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.slot_tw.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.slot_tw.setHorizontalHeaderItem(1, item)
        self.slot_tw.horizontalHeader().setVisible(False)
        self.slot_tw.horizontalHeader().setCascadingSectionResizes(False)
        self.slot_tw.horizontalHeader().setDefaultSectionSize(147)
        self.slot_tw.horizontalHeader().setMinimumSectionSize(93)
        self.slot_tw.verticalHeader().setVisible(False)
        self.slot_tw.verticalHeader().setHighlightSections(False)
        self.verticalLayout_6.addWidget(self.slot_tw)
        self.applySlot_pb = QtWidgets.QPushButton(self.groupBox_6)
        self.applySlot_pb.setObjectName("applySlot_pb")
        self.verticalLayout_6.addWidget(self.applySlot_pb)
        self.horizontalLayout_9.addWidget(self.groupBox_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.nameSearch_le = QtWidgets.QLineEdit(self.groupBox_4)
        self.nameSearch_le.setObjectName("nameSearch_le")
        self.horizontalLayout.addWidget(self.nameSearch_le)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.searchName_pb = QtWidgets.QPushButton(self.groupBox_4)
        self.searchName_pb.setObjectName("searchName_pb")
        self.verticalLayout_3.addWidget(self.searchName_pb)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.slotName_le = QtWidgets.QLineEdit(self.groupBox_3)
        self.slotName_le.setObjectName("slotName_le")
        self.horizontalLayout_3.addWidget(self.slotName_le)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.slotValue_le = QtWidgets.QLineEdit(self.groupBox_3)
        self.slotValue_le.setObjectName("slotValue_le")
        self.horizontalLayout_2.addWidget(self.slotValue_le)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.searchSlot_pb = QtWidgets.QPushButton(self.groupBox_3)
        self.searchSlot_pb.setObjectName("searchSlot_pb")
        self.verticalLayout.addWidget(self.searchSlot_pb)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.horizontalLayout_9.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FrameApp"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Управление фреймами"))
        self.frame_tw.headerItem().setText(0, _translate("MainWindow", "Вывод"))
        self.alg_rb.setText(_translate("MainWindow", "Алгоритм"))
        self.task_rb.setText(_translate("MainWindow", "Задача"))
        self.label_4.setText(_translate("MainWindow", "Название"))
        self.addAlg_pb.setText(_translate("MainWindow", "Добавить"))
        self.remove_pb.setText(_translate("MainWindow", "Удалить"))
        self.getAll_pb.setText(_translate("MainWindow", "Показать всё"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Управление слотами"))
        item = self.slot_tw.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Слот"))
        item = self.slot_tw.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Значение"))
        self.applySlot_pb.setText(_translate("MainWindow", "Применить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Поиск"))
        self.groupBox_4.setTitle(_translate("MainWindow", "По названию"))
        self.label.setText(_translate("MainWindow", "Название"))
        self.searchName_pb.setText(_translate("MainWindow", "Поиск"))
        self.groupBox_3.setTitle(_translate("MainWindow", "По значению слота"))
        self.label_3.setText(_translate("MainWindow", "Слот"))
        self.label_2.setText(_translate("MainWindow", "Значение"))
        self.searchSlot_pb.setText(_translate("MainWindow", "Поиск"))

