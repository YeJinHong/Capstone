import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

# OCR을 위한 Tesseract import
from PIL import Image
from pytesseract import *


class MyMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setexit()
        self.components()
        self.setWindowTitle('Aeye')
        self.setWindowIcon(QIcon('Aeyeicon.png'))
        # self.setGeometry(300, 300, 300, 200)
        self.resize(1000, 800)
        # self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setexit(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

    def components(self):
        wg = MyWidget()
        self.setCentralWidget(wg)


class MyWidget(QWidget):
    filename = ""

    def __init__(self):
        super().__init__()

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('파일을 선택해주세요', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        font1 = self.label1.font()
        self.label1.setFont(font1)
        # 버튼-파일 선택창
        self.btn1 = QPushButton('파일 열기...', self)
        self.btn1.clicked.connect(self.FileOpen)
        # 버튼 - 파일 변환창
        self.btn2 = QPushButton('파일 변환', self)
        self.btn2.clicked.connect(self.FileTrans)
        # 텍스트 출력창
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.text1, 1, 0)
        grid.addWidget(self.btn1, 2, 0)
        grid.addWidget(self.btn2, 1, 1)
        grid.addWidget(QLabel('결과창'), 0, 2)
        grid.addWidget(self.text2, 1, 2)

        self.setGeometry(300, 100, 350, 150)
        self.setWindowTitle("QWidget")
        self.show()

    def FileOpen(self):
        fname = QFileDialog.getOpenFileName(self)
        self.filename = fname[0]
        self.text1.setPlainText('파일이 입력 되었습니다. :\n'+self.filename)

    # 이미지 -> 텍스트 변환 메소드(Tesseract)
    def FileTrans(self):
        # 파일명의 이미지 불러오기
        image = Image.open(self.filename)
        # 텍스트 추출(한글+영어)
        text = image_to_string(image, lang="kor+eng")
        # 텍스트 박스에 있는 내용을 비우고 다시 씀
        self.text2.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
