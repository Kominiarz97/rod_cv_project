import cv2
import imutils
import requests
from db_conn import db_connect
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import edit_image, downsize
from on_rails_anomaly_detection import rails_mask, rails_area, rails_anomaly
from gps import get_position

cap = cv2.VideoCapture('http://192.168.0.100:8080/video')
conn = db_connect()
i = 0
while True:
    if i == 120:
        i = 0
        _, frame = cap.read()
        original = frame.copy()
        resized, edited = edit_image(original)
        rails_org = frame.copy()

        l_x1, r_x1, xl, yl, xr, yr = detect_rails(edited, rails_org)
        if(rails_anomaly(rails_org, original)):
            img_yolo = anomaly_classification(original.copy())
            cv2.putText(img_yolo, "Wykryto anomalie", (60, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2,
                        cv2.LINE_AA)
            #cv2.imshow('YOLO', img_yolo)
            cv2.imwrite("report_photos/img.jpg",img_yolo)

        #rails = downsize(rails_org)
        cv2.imshow("video", frame)
        if cv2.waitKey(22) & 0xFF == ord('q'):
            break

    else:
        i += 1









conn.close()