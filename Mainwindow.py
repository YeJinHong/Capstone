import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, pyqtSlot
from TableWidget import *
import codecs

class MyMainWindow(QMainWindow):
    # save와 save as를 구별하기 위함
    # (True:이미 저장된 파일이 있어 거기에 덮어씌우는 경우/False:처음 저장하는 거라 이름을 지정해줘야 하는 경우)
    savestate = False
    # 새 창의 개수 (워드처럼 새 파일 1 - Aeye 이런 식으로 출력될 수 있게)
    global n
    n = 1

    def __init__(self):
        super().__init__()
        self.initUI()
        self.initmenu()

    def initUI(self):
        self.components()
        self.setWindowTitle("새 파일 " + str(n) +' - Aeye')
        self.setWindowIcon(QIcon('Aeyeicon.png'))
        self.resize(1000, 800)
        self.statusBar()
        # self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initmenu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        # 새로 만들기
        newfileAction = QAction(QIcon('exit.png'), '새로 만들기', self)
        newfileAction.setShortcut('Ctrl+N')
        newfileAction.setStatusTip('새 창을 엽니다.')
        newfileAction.triggered.connect(self.newfile)
        filemenu.addAction(newfileAction)
        # 열기
        fileopenAction = QAction(QIcon('exit.png'), '열기', self)
        fileopenAction.setShortcut('Ctrl+O')
        fileopenAction.setStatusTip('내 PC에서 파일을 불러옵니다.')
        fileopenAction.triggered.connect(self.fileopen)
        filemenu.addAction(fileopenAction)
        # 저장
        filesaveAction = QAction(QIcon('exit.png'), '저장', self)
        filesaveAction.setShortcut('Ctrl+S')
        filesaveAction.setStatusTip('내 PC에 파일을 저장합니다.')
        filesaveAction.triggered.connect(self.filesave)
        # 점자 변환 칸 (tab2.text2)에 내용이 들어가기 전까진 오류 방지를 위해 저장 안 되게
        filesaveAction.setEnabled(False)
        filemenu.addAction(filesaveAction)
        # 다른 이름으로 저장
        filesaveasAction = QAction(QIcon('exit.png'), '다른 이름으로 저장', self)
        filesaveasAction.setShortcut('Ctrl+Shift+S')
        filesaveasAction.setStatusTip('내 PC에 파일을 다른 이름으로 저장합니다.')
        # 점자 변환 칸 (tab2.text2)에 내용이 들어가기 전까진 오류 방지를 위해 저장 안 되게
        filesaveasAction.setEnabled(False)
        filesaveasAction.triggered.connect(self.filesaveas)
        filemenu.addAction(filesaveasAction)
        # 종료
        exitAction = QAction(QIcon('exit.png'), '종료', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램을 종료합니다.')
        exitAction.triggered.connect(qApp.quit)
        filemenu.addAction(exitAction)

    def newfile(self):
        global n
        n += 1
        self.newWindow = MyMainWindow()
        self.newWindow.show()

    def fileopen(self):
        fname = QFileDialog.getOpenFileName(self, self.tr("열기"), "",
                                            self.tr("이미지 파일 (*.jpg *.jpeg *.bmp *.png);;"
                                                    "문서 파일 (*.txt *.docx *.pdf *.hwp *.pptx)"))
        MyTableWidget.filename = fname[0]
        if not fname[0] == "":
            self.setWindowTitle(fname[0]+' - Aeye')
            self.statusBar().showMessage("열림 : " + fname[0])
        self.table_widget.PreView()
        # 파일 변환 버튼에 접근하여 파일을 불러오고 난 후에 버튼 활성화될 수 있게
        self.table_widget.tab1.btn.setEnabled(True)
        self.table_widget.tab2.btn.setEnabled(True)

    def filesave(self):  # 맨 처음의 저장 (다른 이름으로 저장이랑 같은 기능)
        if not self.savestate:
            self.filesaveas()
        else:
            fname = MyTableWidget.filename
            brailleText = self.table_widget.tab2.text2.toPlainText()
            f = open(fname, 'wb')
            f.write(brailleText.encode())
            f.close()
            self.setWindowTitle(fname + ' - Aeye')
            self.statusBar().showMessage("저장됨 : " + fname)

    def filesaveas(self):  # 저장할 파일명을 정하는 다이얼로그가 뜨지 않고 지정된 파일에 덮어씌우는 저장
        fname = QFileDialog.getSaveFileName(self, self.tr("다른 이름으로 저장"), "",
                                            self.tr("점자 파일 (*.bbf *.brf)"))
        # 다른 확장자를 적거나 확장자를 붙이지 않으면 .bbf가 기본값으로 붙고 .bbf, .brf를 확장자로 적으면 그 확장자로 붙음
        if fname[0].split(".")[-1] == "" or fname[0].split(".")[-1] == "bbf" or fname[0].split(".")[-1] == "brf":
            filename = fname[0]
        else:
            filename = fname[0] + ".bbf"
        MyTableWidget.filename = filename
        brailleText = self.table_widget.tab2.text2.toPlainText()
        if not filename == "":
            f = open(filename, 'wb')
            f.write(brailleText.encode())
            f.close()
            self.setWindowTitle(filename + ' - Aeye')
            self.statusBar().showMessage("저장됨 : " + filename)
            self.savestate = True

    def components(self):
        # wg = MyWidget()
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
