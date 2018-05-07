#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
a = QApplication(sys.argv)
hello = QLabel("Hello world!",None)
a.setMainWidget(hello)
hello.show()
a.exec_loop()
