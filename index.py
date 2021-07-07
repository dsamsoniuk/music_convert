#!/usr/bin/env python

import sys
from pydub import AudioSegment
# from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPalette, QIcon

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = "Konwerter muzyki"
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
        self.pathFile = ''
        self.choosenFormat = "mp3"

    def initUI(self):
        self.grid = QGridLayout(self)
        self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setTextTitle("Konwerter formatu dla muzyki", 0)
        self.btnSelect(1)
        self.inputTextPath(2)
        self.setText1("Wybierz format", 3)
        self.selectList(4)
        self.btnConvert(6)
        self.setTextInfo("")
        self.show()

    def setTextTitle(self, value, position):
        self.textTitle = QLabel()
        self.textTitle.setText(value)
        self.grid.addWidget(self.textTitle, position, 0)

    def setText1(self, value, position):
        self.text1 = QLabel()
        self.text1.setText(value)
        self.grid.addWidget(self.text1, position, 0)

    def setTextInfo(self, value):
        self.textInfo = QLabel()
        self.textInfo.setText(value)
        self.grid.addWidget(self.textInfo)

    def selectList(self, position):
        layout = QHBoxLayout()
        self.comboBox = QComboBox()
        self.comboBox.addItems(["mp3", "wav", "mp4", "flv", "avi", "mov"])
        # self.comboBox.addItems(["mp3", "wav", "mp4", "flv", "wma", "avi", "mov"])
        self.comboBox.currentIndexChanged.connect(self.selectionchange)
        self.grid.addWidget(self.comboBox, position, 0)

    def selectionchange(self,i):
        self.choosenFormat = self.comboBox.currentText()
    #   print("Current index",i,"selection changed ",self.comboBox.currentText())

    def inputTextPath(self, position):
        self.inputPathMusic = QLineEdit()
        # line.setValidator(QIntValidator())
        # e1.setMaxLength(4)
        # e1.setAlignment(Qt.AlignRight)
        # line.setFont(QFont("Arial",20))
        self.grid.addWidget(self.inputPathMusic, position , 0)
    def fillPath(self, path):
        self.inputPathMusic.setText(path)
    def btnConvert(self, position):
        button = QPushButton("Konwertuj plik")
        self.grid.addWidget(button, position, 0)
        button.clicked.connect(self.convertMusic)

    def convertMusic(self):
        path = self.pathFile.split("/")
        fileName = path[len(path)-1]
        file = fileName.split(".")
        del path[len(path)-1]
        # print(fileName)
        if self.pathFile == '':
            self.textInfo.setText("Error: Dodaj plik")
        elif len(file) == 2:
            # print('sciezka:' + self.pathFile)
            # print('format plik:' + file[1])
            # print('plik:' + file[0])
            self.textInfo.setText("czekaj ...")
            wav_audio = AudioSegment.from_file(self.pathFile, format=file[1])
            wav_audio.export("/".join(path)+"/" + file[0] + "."+ self.choosenFormat, format=self.choosenFormat)
            self.textInfo.setText("Sukces!")
        else:
            self.textInfo.setText("Error: Nie poprawna sciezka pliku, kropka tylko przy formacie.")

    def btnSelect(self, position):
        button = QPushButton("Wybierz plik")
        self.grid.addWidget(button, position, 0)
        button.clicked.connect(self.selectFile)

    def selectFile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.pathFile = fileName
            self.fillPath(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())


