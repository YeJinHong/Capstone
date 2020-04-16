# coding=utf-8

# GUI를 위한 tkinter import
import tkinter as tk
import tkinter.messagebox as tmsg
from tkinter import *
import tkinter.filedialog as fdialog
from test01 import MyMainWindow
import sys
from PyQt5.QtWidgets import *

# OCR을 위한 Tesseract import
from PIL import Image
from pytesseract import *


# 파일 여는 메소드
def FileOpen():
    # 기본 폴더는 우선 C:\사용자 폴더로 지정되어 있음, 선택할 수 있는 파일 확장자 지정(지원할 파일 확장자가 정확히 정해지면 그때 수정)
    # 파이썬에서는 파일 경로를 표시할 때 \ 대신 / 사용에 주의
    root.filename = fdialog.askopenfilename(initialdir="C:/User", title="파일을 선택해 주세요.",
                                               filetypes=[("모든 그림 파일", "*.jpg *.jpeg *.png *.bmp"), ("모든 파일", "*.*")])
    # 변수 fname에 파일명 저장
    fname = root.filename
    # '파일을 선택해 주세요' 라벨이 있던 자리에 파일명 표시
    fileopen_label.config(text=fname, wraplength=310)


# 이미지 -> 텍스트 변환 메소드(Tesseract)
def ImgToTxt():
    # 파일명의 이미지 불러오기
    image = Image.open(root.filename)
    # 텍스트 추출(한글+영어)
    text = image_to_string(image, lang="kor+eng")
    # 텍스트 박스에 있는 내용을 비우고 다시 씀
    historybox.delete('1.0', tk.END)
    historybox.insert(tk.END, text)


# 메인 프로그램
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyMainWindow()
    sys.exit(app.exec_())
# 메인 프로그램

# 윈도를 만든다
root = tk.Tk()
# 윈도 크기를 변경한다.
root.geometry("600x400")
# 타이틀 이름을 작성한다.
root.title("title입니다.")

# 이력 표시 텍스트 박스를 만듦
historybox = tk.Text(root, font=("Helvetica", 14))
historybox.place(x=350, y=0, width=250, height=400)

# 파일 선택창
fileopen_label = tk.Label(root, text="파일을 선택해 주세요.", font=("Arial", 14))
fileopen_label.place(x=20, y=80)
fileopen_button = tk.Button(root, text="파일 열기...", font=("Helvetica", 10), command=FileOpen)
fileopen_button.place(x=20, y=150)

# 이미지 -> 텍스트 변환(Tesseract)
convert_button = tk.Button(root, text="변환", font=("Helvetica", 10), command=ImgToTxt)
convert_button.place(x=120, y=150)

# 이미지 -> 텍스트 변환(Google Vision)
# client = vision.ImageAnnotatorClient()
