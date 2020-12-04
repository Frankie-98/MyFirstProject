import cv2
cap = cv2.VideoCapture("/dev/video0")
if not cap.isOpened():
    print("cann't open camera!")
cap.set(1, 50)
while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == 'q':
        break