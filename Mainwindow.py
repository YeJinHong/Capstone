import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, pyqtSlot
import Tablewidget

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
        Tablewidget.MyWidget.filename = fname[0]
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
        self.table_widget = Tablewidget.MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
