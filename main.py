from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget,
                             QCheckBox, QFormLayout, QLineEdit, QHBoxLayout, QWidget, QTextBrowser, QGridLayout,
                             QTextEdit, QMessageBox, QShortcut)
import sys
import time
import random
from tasks import questions_answers

class RecipientWindow(QMainWindow):
    button_gen: QPushButton
    button_show_answer: QPushButton
    answerfield: QTextBrowser
    textfield: QTextBrowser
    end_box: QMessageBox
    question: str
    answer: str

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Получатель")
        self.setGeometry(400, 280, 600, 350)
        self.configure_labels()
        self.configure_buttons()
        self.configure_layouts()
        self.QA = questions_answers
        self.shortcut_question = QShortcut(QKeySequence("Ctrl+O"), self)
        self.shortcut_question.activated.connect(self.on_gen)
        self.shortcut_answer = QShortcut(QKeySequence("Ctrl+I"), self)
        self.shortcut_answer.activated.connect(self.on_answer)


    @pyqtSlot()
    def on_gen(self):
        if len(self.QA) > 0:
            self.question, self.answer = random.choice(list(self.QA.items()))
        else:
            self.end_box.show()
        self.textfield.setPlainText(self.question)
        if self.answerfield.toPlainText():
            self.answerfield.clear()
        self.QA.pop(self.question, None)


    @pyqtSlot()
    def on_answer(self):
        if self.textfield.toPlainText():
            self.answerfield.setPlainText(self.answer)

    @pyqtSlot()
    def horrible_ending(self):
        sys.exit()

    def configure_labels(self):
        self.textfield = QTextBrowser()
        self.answerfield = QTextBrowser()
        self.end_box = QMessageBox()
        self.end_box.setIcon(QMessageBox.Information)
        self.end_box.setText("Вопросы закончились")
        self.end_box.setWindowTitle("Душераздирающий конец")
        self.end_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.end_box.buttonClicked.connect(self.horrible_ending)

    def configure_buttons(self):
        self.button_gen = QPushButton('Следующий вопрос', self)
        self.button_gen.clicked.connect(self.on_gen)
        self.button_show_answer = QPushButton('Показать ответ', self)
        self.button_show_answer.clicked.connect(self.on_answer)

    def configure_layouts(self):
        main = QVBoxLayout()
        main.addWidget(self.button_gen)
        main.addWidget(self.button_show_answer)
        main.addWidget(self.textfield)
        main.addWidget(self.answerfield)
        widget = QWidget()
        widget.setLayout(main)
        self.setCentralWidget(widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    recipient = RecipientWindow()
    recipient.show()
    app.exec()

