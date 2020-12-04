import pytesseract
import cv2

path = 'test.png'
img = cv2.imread(path, 0)


def img_recognition(img, lang='chi_sim'):
    code = pytesseract.image_to_string(img, lang)
    print(code)


if __name__ == '__main__':
    img_recognition(img)