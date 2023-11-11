from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Программа")
        self.setGeometry(300, 250, 350, 200)
        self.main_text = QtWidgets.QLabel(self)
        self.new_text = QtWidgets.QLabel(self)

        self.main_text.setText("Надпись")
        self.main_text.move(100, 100)
        self.btn = QtWidgets.QPushButton(self)
        self.btn.setFixedWidth(100)
        self.btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("TEXT")
        self.new_text.move(100, 50)

def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
