from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from instr import*

class FinalWin(QWidget):
    def __init__(self, exp):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
        self.exp()

    def results(self):
        self.exp.age < 7:
            self.index = 0
            return "нет данных для такого возраста"
        self.index = (4 * (int(self.exp.t1) + int(self.exp.t2) + inr(self.exp.t3)) - 200) / 10
        if self.exp.age == 7 or self.exp.age = 8:
            if self.index >= 21:
                return txt_res1
            elif self.index < 21 and self.index >= 17:
                return txt_res2
            elif self.index < 17 and self.index >= 12:
                return txt_res3
            elif self.index < 12 and self.index >= 6.5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 9 or self.exp.age == 10:
            if self.index >= 19.5:
                return txt_res1:
            elif self.index < 19.5 and self.index >= 15.5:
                return txt_res2
            elif self.index < 15.5 and self.index >= 10.5:
                return txt_res3
            elif self.index < 10.5 and self.index >= 5:
                return txt_res4
            else:
                return txt_res5
        if self.exp.age == 11 or self.exp.age == 12:
            if self.index >= 18:
                return txt_res1
            elif self.index < 18 and self.index >= 14:
                return txt_res2
            elif self.index < 12.5 and self.index >= 7.5:
                return txt_res3
            elif self.index < 7.5 and self.index >= 2:
                return txt_res4
            else:
                return txt_res5

        def initUI(self):
            self.work_text = QLabel(txt_workheart + self.results())
            self.index_text - Qlabel(txt_index + str(self.index))
            
            self.layout_line = QVBoxLayout()
            self.layout_line.addWidget(self.index_text, alignment = Qt.AlignCenter)
            self.layout_line.addWidget(self.work_text, alignment = Qt.AlignCenter)
            self.setLayout(self.layout_line)

    def set_appear():
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
