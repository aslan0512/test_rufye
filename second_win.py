
from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont
from PyQt5.QtWidgets import (
        QApplication, QWidget, QLabel,
        QGridLayout, QGroupBox, QListWidget,
        QPushButton, QVBoxLayout, QHBoxLayout,
        QLineEdit, QRadioButton) 

from instr import *
from final_win import *

class Experiment():
    def __init__(self, age, test1, test2, test3):
        self.age = age
        self.t1 = test1
        self.t2 = test2
        self.t3 = test3



class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()  #устанавливает как будет выглядеть окно
        self.initUI()      #создаем и настраиваем графические элементы
        self.connects()    #устанавливает связь между элементами
        self.show()        #старт

    def timer_test(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    
    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)


    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.to.String('hh:mm:ss'))
        self.text_timer.setFont(QFont('Times', 36, QFont.BolD))
        self.text_timer.setStylySheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.to.String('hh:mm:ss')[6:8])
        self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.to.String('hh:mm:ss'))
        if int(time.toString("hh:mm:ss")[6:8]) >= 45:
            self.text_timer.setStylySheet('color: rgb(0, 255, 0)')
        elif int(time.toString("hh:mm:ss")[6:8]) <= 15:
            self.text_timer.setStylySheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet("color: rgb(0,0,0)")
        self.text_timer.setFont(QFont("Times", 36, QFont.Bold))
        if time.toString("hh:mm:ss") == "00:00:00":
            self.timer.stop()


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.text1 = QLabel(txt_name)
        self.text2 = QLabel(txt_age)
        self.text3 = QLabel(txt_test1)
        self.text4 = QLabel(txt_test2)
        self.text5 = QLabel(txt_test3)
        self.text_timer = QLabel(txt_timer)
        self.but1 = QPushButton(txt_starttest1)
        self.but2 = QPushButton(txt_starttest2)
        self.but3 = QPushButton(txt_starttest3)
        self.but4 = QPushButton(txt_sendresults)
        self.input1 = QLineEdit(txt_hintname)
        self.input2 = QLineEdit(txt_hintage)
        self.input3 = QLineEdit(txt_hinttest1)
        self.input4 = QLineEdit(txt_hinttest2)
        self.input5 = QLineEdit(txt_hinttest3)
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignRight)
        self.l_line.addWidget(self.text1, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.input1, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.text2, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.input2, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.text3, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.but1, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.input3, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.text4, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.but2, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.text5, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.but3, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.input4, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.input5, alignment = Qt.AlignTop)
        self.l_line.addWidget(self.but4, alignment = Qt.AlignCenter)
        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    

    def connects(self):
        self.but4.clicked.connect(self.next_click)
        self.but1.clicked.connect(self.timer_test)
        self.but2.clicked.connect(self.timer_sits)
        self.but3.clicked.connect(self.timer_final)


    def next_click(self):
        self.hide()
        self.exp = Experiment(int(self.input2.text()), self.input3.text(), self.input4.text(), self.input5.text())
        self.fw = FinalWin(self.exp)