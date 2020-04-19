# coding = utf-8

from pytesseract import *
import cv2
import re
# 이미지를 화면에 그릴 때만 필요함
import matplotlib.pyplot as plt
import numpy as np

# tesseract 옵션 설정, 언어:한글 (or +영어), psm = 3, 띄어쓰기 보완
config = "-l kor --psm 3 -c preserve_interword_spaces=1"

# 파일명 적기
image_BGR = cv2.imread(r"D:/capstone/unnamed.jpg")
# 이미지를 흑백으로 변경
image_gray = cv2.cvtColor(image_BGR, cv2.COLOR_BGR2GRAY)

# 이미지를 흐릿하게 (가우시안 블러)
image_gray = cv2.GaussianBlur(image_gray, (3,3), 0)

# 이미지의 노이즈 줄이기
image_gray = cv2.fastNlMeansDenoising(image_gray, h=10, searchWindowSize=21, templateWindowSize=7)

# 이미지를 흰색과 검은색으로 임계 전처리
image_gray = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# 좀 더 세부적으로 임계 전처리 (optional)
# image_gray = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 5)

# 화면에 이미지 출력 (optional)
plt.imshow(image_gray, cmap='gray')
plt.show()

# 콘솔에 텍스트 출력
text = image_to_string(image_gray, config=config)
size_table = re.split('\n', text)
print(text)




