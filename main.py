import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
import design  # Это наш конвертированный файл дизайна
from frame_app import *


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = FrameApp()  # Создаём объект класса FrameApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()