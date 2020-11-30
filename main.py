import cv2
import imutils
import requests
from datetime import datetime
import report
from report import report_obstacle
from db_conn import db_connect
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import edit_image, downsize
from on_rails_anomaly_detection import rails_mask, rails_area, rails_anomaly
from gps import get_position


reports = 0
drone_id = 1
conn = db_connect()
if input("Video(1) Zdjecie(2): ") == '1':
    cap = cv2.VideoCapture('http://192.168.0.100:8080/video')

    i = 0

    while True:
        if i == 120:
            i = 0
            _, frame = cap.read()
            original = frame.copy()
            edited, resized = edit_image(original)
            rails_org = frame.copy()

            l_x1, r_x1, xl, yl, xr, yr = detect_rails(edited, rails_org)

            if(rails_anomaly(rails_org, original, 1)):
                img_yolo = anomaly_classification(original.copy())
                cv2.putText(img_yolo, "Wykryto anomalie", (60, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2,
                            cv2.LINE_AA)
                cv2.imwrite(f"report_photos/{drone_id}_{reports}.jpg", img_yolo)
                reports += 1

        else:
            i += 1
        if cv2.waitKey(0) & 0xFF == ord('q'):
            break



else:
    nr = input("Numer zdjecia (1-5): ")

    frame = cv2.imread(f"media/{nr}.JPG")

    original = frame.copy()
    edited, resized = edit_image(original)
    rails_org = frame.copy()
    try:
        l_x1, r_x1, xl, yl, xr, yr = detect_rails(edited, rails_org)
        if (rails_anomaly(rails_org, original, 1)):
            img_yolo = anomaly_classification(original.copy())
            cv2.putText(img_yolo, "Wykryto anomalie", (60, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2,
                        cv2.LINE_AA)
            cv2.imshow('YOLO', img_yolo)
            cv2.imwrite(f"report_photos/{drone_id}_{reports}.jpg", img_yolo)
            report_obstacle(conn,drone_id, reports, 3)
            reports += 1
        else:
            cv2.imshow('YOLO', resized)
        # rails = downsize(rails_org)
        print('Aby wylaczyc wciśnij "q" ')
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
    except:
        print("Nie wykryte tory")
conn.close()