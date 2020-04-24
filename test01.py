import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot

# text_extract.py import
import text_extract as te


class MyMainWindow(QMainWindow):
    savestate = False  # save와 save as를 구별하기 위함

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.components()
        self.setWindowTitle('Aeye')
        self.setWindowIcon(QIcon('Aeyeicon.png'))
        self.resize(1000, 800)
        self.statusBar()
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        self.setnewfile(filemenu)
        self.setfileopen(filemenu)
        self.setfilesave(filemenu)
        self.setfilesaveas(filemenu)
        self.setexit(filemenu)
        # self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setnewfile(self, menu):
        newfileAction = QAction(QIcon('exit.png'), 'New File...', self)
        newfileAction.setShortcut('Ctrl+N')
        # newfileAction.triggered.connect()
        menu.addAction(newfileAction)

    def setfileopen(self, menu):
        fileopenAction = QAction(QIcon('exit.png'), 'Open...', self)
        fileopenAction.setShortcut('Ctrl+O')
        fileopenAction.triggered.connect(self.fileopen)
        menu.addAction(fileopenAction)

    def fileopen(self):
        fname = QFileDialog.getOpenFileName(self, self.tr("열기"), "",
                                            self.tr("이미지 파일 (*.jpg *.jpeg *.bmp *.png);;"
                                                    "문서 파일 (*.txt *.docx *.pdf *.hwp *.pptx)"))
        MyWidget.filename = fname[0]
        self.statusBar().showMessage("열림 : " + fname[0])

    def setfilesave(self, menu):
        filesaveAction = QAction(QIcon('exit.png'), 'Save...', self)
        filesaveAction.setShortcut('Ctrl+S')
        if self.savestate == True:
            filesaveAction.triggered.connect(self.filesave)
        else:
            filesaveAction.triggered.connect(self.filesaveas)
        menu.addAction(filesaveAction)

    def setfilesaveas(self, menu):
        filesaveasAction = QAction(QIcon('exit.png'), 'Save As...', self)
        filesaveasAction.setShortcut('Ctrl+Shift+S')
        filesaveasAction.triggered.connect(self.filesaveas)
        menu.addAction(filesaveasAction)

    def filesave(self):
        self.statusBar().showMessage("저장됨")

    def filesaveas(self):
        fname = QFileDialog.getSaveFileName(self, self.tr("다른 이름으로 저장"), "", self.tr("점자 파일 (*.bbf *.brf)"))
        if not fname:
            return False
        if fname.split(".")[-1] != "bbf":
            fname += ".bbf"
        self.statusBar().showMessage("저장됨 : " + fname[0])
        self.savestate = True

    def setexit(self, menu):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        menu.addAction(exitAction)

    def components(self):
        # wg = MyWidget()
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self);

        # 탭 스크린 설정
        self.tabs = QTabWidget()
        self.tab1 = MyWidget()
        self.tab2 = MyWidget()
        self.tab2.label1.setText("텍스트 입력창")
        self.tab2.label2.setText("점자 결과창")
        self.tab2.text1.setText(self.tab1.text2.toPlainText())
        self.tabs.resize(1000, 800)
        self.tabs.addTab(self.tab1, "image -> text")
        self.tabs.addTab(self.tab2, "text -> brail text")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    """ #참조 블로그에 있던 메소드. 무슨 용도인지 모르겠음.
    @pyqtSlot()
    def on_click(self):
        print("/n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    """


class MyWidget(QWidget):
    filename = ""

    def __init__(self):
        super().__init__()

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('파일 입력창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label2 = QLabel('텍스트 결과창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        # 버튼 - 파일 변환창
        self.btn2 = QPushButton('파일 변환', self)
        self.btn2.clicked.connect(self.WriteText)
        # 텍스트 출력창
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()

        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.text1, 1, 0)
        grid.addWidget(self.btn2, 1, 1)
        grid.addWidget(self.label2, 0, 2)
        grid.addWidget(self.text2, 1, 2)

        self.setGeometry(300, 100, 350, 150)
        self.setWindowTitle("QWidget")
        self.show()

    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        text = te.ReturnText(self.filename)
        # text2 창에 읽어온 텍스트를 출력
        self.text2.setPlainText(text)
        # MyTableWidget._init__.tab1.text2.setPlainText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
