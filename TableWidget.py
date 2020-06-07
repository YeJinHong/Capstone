import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import convertor
import TextArea
from I2Twidget import I2TWidget
from T2Bwidget import T2Bwidget


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



        self.tabs.resize(1000, 800)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

        self.tabs.currentChanged.connect(self.setText)

    def setText(self):
        self.tab2.text1.setPlainText(self.tab1.text2.toPlainText())


