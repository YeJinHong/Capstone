import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import *

import text_extract as te
import convertor


class MyTableWidget(QWidget):
    filename = ""
    cropped_filename = ""

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self);

        # 탭 스크린 설정
        self.tabs = QTabWidget()
        self.tab1 = MyWidget()
        self.tab1.label1.setText("파일 입력창")
        self.tab1.label2.setText("텍스트 결과창")
        self.tab1.grid.addWidget(self.tab1.label_picture, 1, 0)
        self.tab1.btn_crop = QPushButton('이미지 부분 인식', self)
        self.tab1.btn_crop.setEnabled(False)
        self.tab1.grid.addWidget(self.tab1.btn_crop, 2, 0)
        self.tab1.btn_crop.clicked.connect(self.imageShow)
        self.tab1.btn_crop.setStatusTip("이미지를 드래그하여 인식하고 싶은 부분만을 인식합니다.")
        self.tab2 = MyWidget()
        self.tab2.label1.setText("텍스트 입력창")
        self.tab2.label2.setText("점자 결과창")
        self.tab2.label_picture.setParent(None)
        self.tab2.grid.addWidget(self.tab2.text1, 1, 0)
        self.tabs.resize(1000, 800)
        self.tabs.addTab(self.tab1, "image -> text")
        self.tabs.addTab(self.tab2, "text -> braille text")
        self.tab1.btn.clicked.connect(self.WriteText)
        self.tab1.btn.setStatusTip("이미지에서 텍스트를 추출합니다.")
        self.tab1.btn.setEnabled(False)
        self.tab2.btn.clicked.connect(self.WriteBraille)
        self.tab2.btn.setStatusTip("텍스트를 점자로 변환합니다.")
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        if self.cropped_filename != "":
            text = te.ReturnText(self.cropped_filename)
        else:
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
        result = convertor.ko_braile_convertor(text)
        self.tab2.text2.setPlainText(result)
        bfont = QFont("Braille from BRL2000", 15)
        self.tab2.text2.setFont(bfont)

    def imageShow(self):
        global isDragging, x0, y0, img
        isDragging = False
        x0, y0, w, h = -1, -1, -1, -1

        def onMouse(event, x, y, flags, param):
            global isDragging, x0, y0, img
            if event == cv2.EVENT_LBUTTONDOWN:
                isDragging = True
                x0 = x
                y0 = y
            elif event == cv2.EVENT_MOUSEMOVE:
                if isDragging:
                    img_draw = img.copy()
                    cv2.rectangle(img_draw, (x0, y0), (x, y), (0, 0, 255), 3)
                    cv2.imshow('Drag to crop image', img_draw)
            elif event == cv2.EVENT_LBUTTONUP:
                if isDragging:
                    isDragging = False
                    w = x - x0
                    h = y - y0
                    if w > 0 and h > 0:
                        img_draw = img.copy()
                        cv2.rectangle(img_draw, (x0, y0), (x, y), (0, 0, 255), 3)
                        temp = cv2.rectangle(img_draw, (x0, y0), (x, y), (0, 0, 255), 3)
                        xy = "(" + str(x0) + "," + str(y0) + ")"
                        if y0 < 15:
                            cv2.putText(temp, xy, (x0, y0 + 15), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                        else:
                            cv2.putText(temp, xy, (x0, y0 - 15), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                        cv2.imshow('Drag to crop image', img_draw)
                        roi = img[y0:y0 + h, x0:x0 + w]
                        cv2.imshow('Cropped image', roi)
                        cv2.moveWindow('Cropped image', 100, 100)
                        cv2.imwrite('./cropped.png', roi)
                        self.cropped_filename = './cropped.png'
                        '''self.tab1.qPixmapFileVar.load(self.filename)
                        self.tab1.qPixmapFileVar = self.tab1.qPixmapFileVar.scaledToWidth(400)
                        self.tab1.label_picture.setPixmap(self.tab1.qPixmapFileVar)'''
                else:
                    cv2.imshow('Drag to crop image', img)
                    print('drag should start from left-top side')

        img = cv2.imread(self.filename)
        # 원본 이미지가 너무 크면 리사이징?
        '''height, width, channel = img.shape
        if height > 1020 or width > 1680:
            img = cv2.resize(img, (int(width/1.5), int(height/1.5)))'''
        cv2.imshow('Drag to crop image', img)
        cv2.setMouseCallback('Drag to crop image', onMouse)
        cv2.waitKey()
        cv2.destroyAllWindows()

class MyWidget(QWidget):
    filename = ""

    def __init__(self):
        super().__init__()

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('입력창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label2 = QLabel('결과창', self)
        self.label2.setAlignment(Qt.AlignVCenter)
        # 버튼 - 파일 변환창
        self.btn = QPushButton('파일 변환', self)

        # 이미지 출력창
        self.label_picture = QLabel('이미지 출력창', self)
        self.label_picture.setFixedWidth(400)
        self.label_picture.setStyleSheet("QLabel { background-color : grey; }")
        self.label_picture.setAlignment(Qt.AlignCenter)

        # 텍스트 출력창
        self.text1 = QTextEdit()
        self.text2 = QTextEdit()

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label1, 0, 0, Qt.AlignCenter)

        # self.grid.addWidget(self.text1, 1, 0)
        self.grid.addWidget(self.btn, 1, 1)
        self.grid.addWidget(self.label2, 0, 2, Qt.AlignCenter)
        self.grid.addWidget(self.text2, 1, 2)

        self.setGeometry(300, 100, 350, 150)
        #self.setWindowTitle("QWidget")
        self.show()