import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 라벨-파일 선택 안내문
        label1 = QLabel('파일을 선택해주세요', self)
        label1.setAlignment(Qt.AlignVCenter)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)
        label1.move(100, 100)
        #버튼-파일 선택창
        btn1 = QPushButton('파일 열기...', self)
        btn1.move(100, 200)
        #텍스트 출력창
        te = QTextEdit()
        te.move(300, 100)

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)


        #상태바
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Aeye')
        self.setWindowIcon(QIcon('Aeyeicon.png'))
        self.resize(600, 400)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())