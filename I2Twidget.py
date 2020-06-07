import cv2
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QCheckBox, QMessageBox
import TextArea
import text_extract as te


class I2TWidget(QWidget):


    def __init__(self):
        super().__init__()

        self.filename = ""
        self.cropped_filename = ""
        self.cropped = False

        # 라벨-파일 선택 안내문
        self.label1 = QLabel('파일 입력창', self)
        self.label1.setAlignment(Qt.AlignVCenter)
        self.label2 = QLabel('텍스트 결과창', self)
        self.label2.setAlignment(Qt.AlignVCenter)

        # 이미지 출력창
        self.label_picture = QLabel('이미지 출력창', self)
        self.label_picture.setFixedWidth(400)
        self.label_picture.setStyleSheet("QLabel { background-color : grey; }")
        self.label_picture.setAlignment(Qt.AlignCenter)

        # 버튼 - 파일 변환창
        self.btn = QPushButton('파일 변환', self)
        self.btn.clicked.connect(self.WriteText)
        # 텍스트 출력창
        self.text2 = TextArea.QCodeEditor()

        # 이미지 부분 추출 버튼
        self.btn_crop = QPushButton('이미지 부분 인식', self)
        self.btn_crop.setEnabled(False)
        self.btn_crop.clicked.connect(self.imageShow)
        self.btn_crop.setStatusTip("이미지를 드래그하여 인식하고 싶은 부분만을 인식합니다.")

        # 결과창 초기화 버튼
        self.btn_clear = QPushButton('초기화', self)
        self.btn_clear.clicked.connect(self.clearText)
        self.btn_clear.setStatusTip("텍스트 결과창 내의 텍스트를 초기화합니다.")

        # 이미지 이어쓰기 확인 체크 박스
        self.check = QCheckBox('이어쓰기', self)
        self.check.setStatusTip("이어쓰기 모드를 활성화/비활성화합니다.")
        self.check.setEnabled(False)

        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.grid.addWidget(self.label1, 0, 0, Qt.AlignCenter)
        self.grid.addWidget(self.label2, 0, 2, Qt.AlignCenter)
        self.grid.addWidget(self.check, 0, 1)
        self.grid.addWidget(self.label_picture, 1, 0)
        self.grid.addWidget(self.btn, 1, 1)
        self.grid.addWidget(self.text2, 1, 2)
        self.grid.addWidget(self.btn_crop, 2, 0)
        self.grid.addWidget(self.btn_clear, 2, 2)

        self.setGeometry(300, 100, 350, 150)
        self.show()

    def imageShow(self):
        global isDragging, x0, y0, img
        isDragging = False
        x0, y0, w, h = -1, -1, -1, -1

        def onMouse(event, x, y, flags, param):
            global isDragging, x0, y0, img
            height, width, channel = img.shape
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
                    if x < x0:
                        t = x
                        x = x0
                        x0 = t
                    if y < y0:
                        t = y
                        y = y0
                        y0 = t
                    w = abs(x - x0)
                    h = abs(y - y0)
                    img_draw = img.copy()
                    cv2.rectangle(img_draw, (x0, y0), (x, y), (0, 0, 255), 3)
                    temp = cv2.rectangle(img_draw, (x0, y0), (x, y), (0, 0, 255), 3)
                    xy = "(" + str(x0) + "," + str(y0) + ")"
                    xy2 = "(" + str(x) + "," + str(y) + ")"
                    if y0 < int(height/20*3):
                        cv2.putText(temp, xy, (x0, y0 + 25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                        cv2.putText(temp, xy2, (x-120, y+25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                    elif y > int(height/20*17):
                        cv2.putText(temp, xy, (x0, y0 - 15), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                        cv2.putText(temp, xy2, (x - 120, y - 15), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                    else:
                        cv2.putText(temp, xy, (x0, y0 - 15), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                        cv2.putText(temp, xy2, (x-120, y+25), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 0, 255), 2)
                    cv2.imshow('Drag to crop image', img_draw)
                    roi = img[y0:y0 + h, x0:x0 + w]
                    cv2.imshow('Cropped image', roi)
                    cv2.moveWindow('Cropped image', 100, 100)
                    message = QMessageBox().question(self, 'Cropped image', xy+', '+xy2+' - 이 이미지로 하시겠습니까?',
                                                              QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if message == QMessageBox.Yes:
                        cv2.imwrite('./cropped.png', roi)
                        self.cropped_filename = './cropped.png'
                        cv2.destroyWindow('Drag to crop image')
                        self.cropped = True
                    else:
                        cv2.destroyWindow('Cropped image')
            else:
                cv2.imshow('Drag to crop image', img)
                print('drag should start from left-top side')

        img = cv2.imread(self.filename)
        # 원본 이미지가 너무 크면 리사이징?
        '''
        if height > 1020 or width > 1680:
            img = cv2.resize(img, (int(width/1.5), int(height/1.5)))'''
        cv2.imshow('Drag to crop image', img)
        cv2.setMouseCallback('Drag to crop image', onMouse)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def clearText(self):
        self.text2.setPlainText("")

    def PreView(self):
        # QPixmap 객체 생성 후 이미지 파일 데이터 로드, Label을 이용하여 화면에 표시
        self.qPixmapFileVar = QPixmap()
        self.qPixmapFileVar.load(self.filename)
        self.qPixmapFileVar = self.qPixmapFileVar.scaledToWidth(400)
        self.label_picture.setPixmap(self.qPixmapFileVar)\

# 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        if self.check.isChecked():  # 이어쓰기 모드 활성화
            self.text = self.text2.toPlainText()
            if self.cropped_filename != "":
                txt = te.ReturnText(self.cropped_filename)
                self.cropped_filename = ""
            else:
                txt = te.ReturnText(self.filename)
            # text2 창에 읽어온 텍스트를 출력
            if self.text == "" or self.text == "텍스트를 발견하지 못했습니다." \
                    or self.text == "변환할 수 없는 파일입니다.\n지원하는 파일 타입은 이미지 파일 또는 텍스트 파일입니다.\n다시 시도해 주십시오.":
                self.text2.setPlainText(txt)
                #self.tab2.text1.setPlainText(txt)
            else:
                self.text2.setPlainText(self.text+'\n\n'+txt)
                #self.tab2.text1.setPlainText(self.text+'\n\n'+txt)
        else:  # 이어쓰기 모드 비활성화
            self.text = ""
            if self.cropped_filename != "":
                txt = te.ReturnText(self.cropped_filename)
            else:
                txt = te.ReturnText(self.filename)
            # text2 창에 읽어온 텍스트를 출력
            self.text2.setPlainText(txt)

