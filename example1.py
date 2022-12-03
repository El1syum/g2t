import sys
from PyQt5.QtWidgets import QApplication, QWidget


# TODO Сделать через класс
class TODO(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Hello world')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # Параметр sys.argv — это список аргументов из командной строки.
    a = TODO()
    sys.exit(app.exec_())  # Наконец, мы входим в главный цикл приложения.
