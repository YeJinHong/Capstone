import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import convertor
import TextArea
from I2Twidget import I2TWidget
from T2Bwidget import T2Bwidget

import text_extract as te


class MyTableWidget(QWidget):
    filename = ""
    cropped_filename = ""

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self);


        self.text = ""
        # 탭 스크린 설정
        self.tabs = QTabWidget()
        self.tab1 = I2TWidget()
        self.tab2 = T2Bwidget()
        self.tabs.addTab(self.tab1, "image -> text")
        self.tabs.addTab(self.tab2, "text -> braille text")

        self.tab1.btn.clicked.connect(self.WriteText)

        self.tabs.resize(1000, 800)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    def WriteText(self):
        # 파일로부터 텍스트를 읽어옴
        if self.tab1.check.isChecked():  # 이어쓰기 모드 활성화
            self.text = self.tab1.text2.toPlainText()
            if self.tab1.cropped:
                txt = te.ReturnText(self.tab1.cropped_filename)
                self.cropped_filename = ""
            else:
                txt = te.ReturnText(self.filename)
            # text2 창에 읽어온 텍스트를 출력
            if self.text == "" or self.text == "텍스트를 발견하지 못했습니다." \
                    or self.text == "변환할 수 없는 파일입니다.\n지원하는 파일 타입은 이미지 파일 또는 텍스트 파일입니다.\n다시 시도해 주십시오.":
                self.tab1.text2.setPlainText(txt)
                self.tab2.text1.setPlainText(txt)
            else:
                self.tab1.text2.setPlainText(self.text+'\n\n'+txt)
                self.tab2.text1.setPlainText(self.text+'\n\n'+txt)
        else:  # 이어쓰기 모드 비활성화
            self.text = ""
            if self.tab1.cropped:
                txt = te.ReturnText(self.tab1.cropped_filename)
            else:
                txt = te.ReturnText(self.filename)
            # text2 창에 읽어온 텍스트를 출력
            self.tab1.text2.setPlainText(txt)
            self.tab2.text1.setPlainText(txt)
