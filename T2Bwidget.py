
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout
import TextArea
import convertor


class T2Bwidget(QWidget):
    filename = ""

    def __init__(self):
        super().__init__()

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('텍스트 입력창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label2 = QLabel('점자 결과창', self)
        self.label2.setAlignment(Qt.AlignVCenter)
        # 버튼 - 파일 변환창
        self.btn = QPushButton('파일 변환', self)
        self.btn.clicked.connect(self.WriteBraille)

        # 결과창 초기화 버튼
        self.btn_clear = QPushButton('초기화', self)

        # 이미지 출력창
        self.label_picture = QLabel('이미지 출력창', self)
        self.label_picture.setFixedWidth(400)
        self.label_picture.setStyleSheet("QLabel { background-color : grey; }")
        self.label_picture.setAlignment(Qt.AlignCenter)
        self.label_picture.setParent(None)

        # 텍스트 출력창
        self.text1 = TextArea.QCodeEditor()
        self.text2 = TextArea.QCodeEditor()

        self.btn_clear.clicked.connect(self.clearBraille)
        self.btn_clear.setStatusTip("점자 결과창 내의 점자 텍스트를 초기화합니다.")

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label1, 0, 0, Qt.AlignCenter)
        self.grid.addWidget(self.label2, 0, 2, Qt.AlignCenter)
        self.grid.addWidget(self.text1, 1, 0)
        self.grid.addWidget(self.btn, 1, 1)
        self.grid.addWidget(self.text2, 1, 2)
        self.grid.addWidget(self.btn_clear, 2, 2)

        self.setGeometry(300, 100, 350, 150)
        self.show()

    def clearBraille(self):
        self.text2.setPlainText("")

    # 텍스트 박스에 있는 내용을 점자로 바꿔 씀
    def WriteBraille(self):
        text = self.text1.toPlainText()
        result = convertor.ko_braile_convertor(text)
        self.text2.setPlainText(result)
        bfont = QFont("Braille from BRL2000", 15)
        self.text2.setFont(bfont)