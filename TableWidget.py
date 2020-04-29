from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import *

import text_extract as te


class MyTableWidget(QWidget):
    filename = ""

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self);

        # 탭 스크린 설정
        self.tabs = QTabWidget()
        self.tab1 = MyWidget()
        self.tab1.label1.setText("파일 입력창")
        self.tab1.label2.setText("텍스트 결과창")
        self.tab1.grid.addWidget(self.tab1.label_picture, 1, 0)
        self.tab2 = MyWidget()
        self.tab2.label1.setText("텍스트 입력창")
        self.tab2.label2.setText("점자 결과창")
        self.tab2.label_picture.setParent(None)
        self.tab2.grid.addWidget(self.tab2.text1, 1, 0)
        self.tabs.resize(1000, 800)
        self.tabs.addTab(self.tab1, "image -> text")
        self.tabs.addTab(self.tab2, "text -> braille text")
        self.tab1.btn.clicked.connect(self.WriteText)
        self.tab2.btn.clicked.connect(self.WriteBraille)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        text = te.ReturnText(self.filename)
        # text2 창에 읽어온 텍스트를 출력
        self.tab1.text2.setPlainText(text)
        self.tab2.text1.setPlainText(text)

    def PreView(self):
        # QPixmap 객체 생성 후 이미지 파일 데이터 로드, Label을 이용하여 화면에 표시
        self.tab1.qPixmapFileVar = QPixmap()
        self.tab1.qPixmapFileVar.load(self.filename)
        self.tab1.qPixmapFileVar = self.tab1.qPixmapFileVar.scaledToWidth(400)
        self.tab1.label_picture.setPixmap(self.tab1.qPixmapFileVar)

    # 텍스트 박스에 있는 내용을 점자로 바꿔 씀
    def WriteBraille(self):
        text = self.tab2.text1.toPlainText()

        self.tab2.text2.setText(text)


class MyWidget(QWidget):
    filename = ""

    def __init__(self):
        super().__init__()

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('입력창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label2 = QLabel('결과창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        # 버튼 - 파일 변환창
        self.btn = QPushButton('파일 변환', self)
        # 이미지 출력창
        self.label_picture = QLabel('이미지 출력창', self)
        # 텍스트 출력창
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()
        #버튼 - 프린터 생성
        self.btn_p = QPushButton('Print PDF File', self)
        self.btn_p.clicked.connect(self.btnClickPrint)

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label1, 0, 0)
        #self.grid.addWidget(self.text1, 1, 0)
        self.grid.addWidget(self.btn, 1, 1)
        self.grid.addWidget(self.label2, 0, 2)
        self.grid.addWidget(self.text2, 1, 2)
        self.grid.addWidget(self.btn_p, 2, 0)

        self.setGeometry(300, 100, 350, 150)
        #self.setWindowTitle("QWidget")
        self.show()

    # 프린터 생성, 실행
    def btnClickPrint(self):
        printer = QPrinter()
        dlg = QPrintDialog(printer, self)
        if dlg.exec() == QDialog.Accepted:
            #Painter 생성
            qp = QPainter()
            qp.begin(printer)

            # 여백 비율
            wgap = printer.pageRect().width() * 0.1
            hgap = printer.pageRect().height() * 0.1

            # 화면 중앙에 위젯 배치
            xscale = (printer.pageRect().width() - wgap) / self.table.width()
            yscale = (printer.pageRect().height() - hgap) / self.table.height()
            scale = xscale if xscale < yscale else yscale
            qp.translate(printer.paperRect().x() + printer.pageRect().width() / 2,
                         printer.paperRect().y() + printer.pageRect().height() / 2)
            qp.scale(scale, scale);
            qp.translate(-self.table.width() / 2, -self.table.height() / 2);

            # 인쇄
            self.table.render(qp)

            qp.end()