import cv2
import numpy as np
from OCR import img_recognition
myColor = [0, 211, 145, 77, 255, 255]

myColorValue = [0, 0, 255]


def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array(myColor[0:3])
    upper = np.array(myColor[3:6])
    mask = cv2.inRange(imgHSV, lower, upper)
    x, y, w, h = getContours(mask)
    if x != 0 and y != 0:
        cv2.circle(imgResult, (x, y), 3, myColorValue, cv2.FILLED)
        return [x, y, x + w, y + h]
    else:
        return None


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 1)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x, y, w, h


def drawOnCanvas(point, myColorValues):
    if point is None:
        print("请用红笔指向文字的起点！")
    else:
        cv2.rectangle(imgResult, (point[0], point[1]), (point[2] + 300, point[3]), myColorValues, 2)
        print(point[0], point[1], point[2], point[3])
        return point[0], point[1], point[2] + 300, point[3]


cap = cv2.VideoCapture(0)
cap.set(10, 20)  # 亮度

while True:
    success, img = cap.read()
    xImg = cv2.flip(img, 1, dst=None)
    imgGray = cv2.cvtColor(xImg, cv2.COLOR_BGRA2GRAY)
    imgResult = xImg.copy()
    newPoint = findColor(xImg)
    if drawOnCanvas(newPoint, myColorValue) is not None:
        x0, y0, x1, y1 = drawOnCanvas(newPoint, myColorValue)
        imgCropped = imgGray[y0:y1, x0:x1]
        cv2.imshow("Croped", imgCropped)
        img_recognition(imgCropped)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
