import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QPainter

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
        self.tab2 = MyWidget()
        self.tab2.label1.setText("텍스트 입력창")
        self.tab2.label2.setText("점자 결과창")
        self.tab2.text1.setText(self.tab1.text2.toPlainText())
        self.tabs.resize(1000, 800)
        self.tabs.addTab(self.tab1, "image -> text")
        self.tabs.addTab(self.tab2, "text -> brail text")
        self.tab1.btn.clicked.connect(self.WriteText)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        text = te.ReturnText(self.filename)
        # text2 창에 읽어온 텍스트를 출력
        self.text2.setPlainText(text)
        self.tab2.text1.setPlainText(text)


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
        # 텍스트 출력창
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()

        #버튼 - 프린터 생성
        self.btn_p = QPushButton('Print PDF File', self)
        self.btn_p.clicked.connect(self.btnClickPrint)

        #슬라이더 - 확대 축소 기능
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setRange(8, 30)
        self.slider.setSingleStep(2)
        self.slider.valueChanged.connect(self.font_slider)

        #슬라이더 값에 따라 text1의 폰트 크기 조절


        grid = QGridLayout()
        self.setLayout(grid)
        grid.addWidget(self.label1, 0, 0)
        grid.addWidget(self.text1, 1, 0)
        grid.addWidget(self.btn, 1, 1)
        grid.addWidget(self.label2, 0, 2)
        grid.addWidget(self.text2, 1, 2)
        grid.addWidget(self.btn_p, 2, 0)
        grid.addWidget(self.slider, 2, 2)

        self.setGeometry(300, 100, 350, 150)
        #self.setWindowTitle("QWidget")
        self.show()


    # 확대 축소 기능을 폰트 조절로 구현하려 했으나 에러 발생
    def font_slider(self):
        self.text1.setFontPointSize(self, self.slider.value)

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