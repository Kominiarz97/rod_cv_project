import cv2
import requests
cap = cv2.VideoCapture('http://192.168.0.100:8080/video')
while True:
    _, frame = cap.read()
    cv2.imshow("video",frame)
    if cv2.waitKey(22) & 0xFF == ord('q'):
        break
