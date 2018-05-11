# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_set_algs.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialogAlgs(object):
    def setupUi(self, dialogAlgs):
        dialogAlgs.setObjectName("dialogAlgs")
        dialogAlgs.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dialogAlgs.sizePolicy().hasHeightForWidth())
        dialogAlgs.setSizePolicy(sizePolicy)
        dialogAlgs.setMinimumSize(QtCore.QSize(400, 200))
        dialogAlgs.setMaximumSize(QtCore.QSize(400, 200))
        self.buttonBox = QtWidgets.QDialogButtonBox(dialogAlgs)
        self.buttonBox.setGeometry(QtCore.QRect(308, 9, 83, 61))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.algs_lv = QtWidgets.QListView(dialogAlgs)
        self.algs_lv.setGeometry(QtCore.QRect(0, 10, 291, 181))
        self.algs_lv.setObjectName("algs_lv")

        self.retranslateUi(dialogAlgs)
        self.buttonBox.rejected.connect(dialogAlgs.reject)
        self.buttonBox.accepted.connect(dialogAlgs.accept)
        QtCore.QMetaObject.connectSlotsByName(dialogAlgs)

    def retranslateUi(self, dialogAlgs):
        _translate = QtCore.QCoreApplication.translate
        dialogAlgs.setWindowTitle(_translate("dialogAlgs", "Algorithms setter"))

