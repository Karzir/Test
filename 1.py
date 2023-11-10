import sys
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()
        self.f = False

    def initUI(self):
        self.setWindowTitle('Рисование')
        self.pushButton.clicked.connect(self.qwe)

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y, r = randint(0, 700), randint(0, 500), randint(1, 100)
        qp.drawEllipse(x, y, r, r)
    def qwe(self):
        self.f = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
