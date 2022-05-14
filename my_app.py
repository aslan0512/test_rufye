from PyQt5.QtCore import Qt  

from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QVBoxLayout,QHBoxLayout

from PyQt5.QtGui import QFont
from instr import *
from second_win import *




class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.btn_next = QPushButton(txt_next)
        self.hello_text = QLabel(txt_hello)
        self.instruction = QLabel(txt_instruction)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.instruction,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.btn_next,alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    def connects(self):
        self.btn_next.clicked.connect(self.next_clicked)

    def next_clicked(self):
        self.tw = TestWin()
        self.hide
        

app = QApplication([])
mv = MainWin()
app.exec_()
