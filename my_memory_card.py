#create a memory card application

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QVBoxLayout, QHBoxLayout, QMessageBox, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main_win = QWidget()

class Question():
    def __init__(self, question, Right, Wrong1, Wrong2, Wrong3):
        self.question = question
        self.Right = Right
        self.Wrong1 = Wrong1
        self.Wrong2 = Wrong2
        self.Wrong3 = Wrong3

questions = list()
q1 = Question("What is the bigest battle ship?", "Yamato", "Uss Missor", "Uss Zumwalt", "RF ADMIRAL KUZNETSOV")

questions.append(q1)

q2 = Question("Who are you, i don't now you,why are you now my name?", "order", "...", "i don't now you", "do not thing")
questions.append(q2)

q3 = Question("Thủ đô  của Việt Nam ở đâu?", "Hà Nội", "Thành phố Hồ Chí Minh", "Hải Phòng", "Trường Sa - Hoàng Sa")
questions.append(q3)

qt = QLabel("What is the bigest battle ship?")

time_labal = QLabel('Time:')
timer = QLabel("0")
time_amount = 250
timer.setText(str(time_amount))

btn1 = QRadioButton("Yamato")
btn2 = QRadioButton("Uss Missor")
btn3 = QRadioButton("Uss Zumwalt")
btn4 = QRadioButton("RF ADMIRAL KUZNETSOV")

RdoG = QButtonGroup()
RdoG.addButton(btn1)
RdoG.addButton(btn2)
RdoG.addButton(btn3)
RdoG.addButton(btn4)

btn_ans = QPushButton("Answer")

vtc_lo = QVBoxLayout()

lo_qt = QHBoxLayout()
hlo1 = QHBoxLayout()
hlo2 = QHBoxLayout()
lo_ans = QHBoxLayout()
lo_tm = QHBoxLayout()

lo_qt.addWidget(qt, alignment = Qt.AlignCenter)

hlo1.addWidget(btn1, alignment = Qt.AlignCenter)
hlo1.addWidget(btn2, alignment = Qt.AlignCenter)

hlo2.addWidget(btn3, alignment = Qt.AlignCenter)
hlo2.addWidget(btn4, alignment = Qt.AlignCenter)

lo_ans.addWidget(btn_ans, alignment = Qt.AlignCenter)

lo_tm.addWidget(time_labal, alignment = Qt.AlignLeft)
lo_tm.addWidget(timer, alignment = Qt.AlignLeft, stretch = 1)



RdoGB = QGroupBox("Answer option")
lo_rdo = QVBoxLayout()

lo_rdo.addLayout(hlo1)
lo_rdo.addLayout(hlo2)

RdoGB.setLayout(lo_rdo)

RstGB = QGroupBox("Test result")
lo_rst = QVBoxLayout()

lb_rst = QLabel("Icorrect answer !!!")
lb_crrc = QLabel("Correct answer !!!")

lo_rst.addWidget(lb_rst, alignment = (Qt.AlignLeft | Qt.AlignTop))
lo_rst.addWidget(lb_crrc, alignment = Qt.AlignHCenter, stretch = 2)

RstGB.setLayout(lo_rst)

lo_gb = QHBoxLayout()
lo_gb.addWidget(RdoGB)
lo_gb.addWidget(RstGB)
RstGB.hide()

vtc_lo.addLayout(lo_tm)
vtc_lo.addLayout(lo_qt)
vtc_lo.addLayout(lo_gb)
vtc_lo.addLayout(lo_ans)

def show_result():
    RdoGB.hide()
    RstGB.show()
    btn_ans.setText("??? Next Question ??????? !!!")

def show_question():
    RdoGB.show()
    RstGB.hide()
    btn_ans.setText("Answer")
    RdoG.setExclusive(False)
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RdoG.setExclusive(True)

ans_lst = [btn1, btn2, btn3, btn4]
def ask(q: Question):
    qt.setText(q.question)

    shuffle(ans_lst)
    ans_lst[0].setText(q.Right)
    ans_lst[1].setText(q.Wrong1)
    ans_lst[2].setText(q.Wrong2)
    ans_lst[3].setText(q.Wrong3)

    lb_crrc.setText("Correct answer:" + q.Right)
    show_question()

def show_correct(result):
    lb_rst.setText(result)
    show_result()

def check_ans():
    if ans_lst[0].isChecked():
        show_correct("Correct !!!!!!!!!!!!!!!!!!!!!!")
    else:
        if ans_lst[1].isChecked() or ans_lst[2].isChecked() or ans_lst[3].isChecked():
            show_correct("Incorrect !!?!")
        

def next_question():
    cur_question = randint(0, len(questions)-1)
    q = questions[cur_question]
    ask(q)

def click_button():
    if btn_ans.text() == "??? Next Question ??????? !!!":
        next_question()
    else:
        check_ans()

def show_time():
    global time_amount
    time_amount -= 1
    if time_amount == 0:
        print("Times'up!!!!!!?!?!?!!?!!??!?")
        app.quit()
    timer.setText(str(time_amount))

timer_clk = QTimer()
timer_clk.timeout.connect(show_time)
timer_clk.start(100)


ask(q1)
btn_ans.clicked.connect(click_button)
next_question()
main_win.setLayout(vtc_lo)
main_win.setWindowTitle("Memory Card")
main_win.resize(1999,893)
main_win.show()
app.exec()