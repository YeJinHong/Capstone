from pytesseract import *
import cv2

def ImagetoText(fileName):
    # 이미지 불러오기
    image = cv2.imread(fileName)

    # 이미지를 흑백으로 변경
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 이미지를 흐릿하게 (가우시안 블러)
    image_blurred = cv2.GaussianBlur(image_gray, (3, 3), 0)

    # 이미지의 노이즈 줄이기
    image_denoising = cv2.fastNlMeansDenoising(image_blurred, h=10, searchWindowSize=21, templateWindowSize=7)

    # 이미지를 흰색과 검은색으로 임계 전처리
    image_final = cv2.threshold(image_denoising, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # tesseract 옵션 설정, 언어:한글 (or +영어), psm = 3, 띄어쓰기 보완
    config = "-l kor --psm 3 -c preserve_interword_spaces=1"

    # 텍스트 추출
    text = image_to_string(image_final, config=config)
    return text

def TexttoText(fileName):
    text = fileName.read()
    return text

if __name__ == "__main__":
    print("this is ocr.py")
