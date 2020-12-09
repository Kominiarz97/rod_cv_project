import cv2
from time import sleep
from report import report_obstacle
from db_conn import db_connect
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import edit_simple, edit_image
from on_rails_anomaly_detection import rails_mask, rails_area, rails_anomaly

conn = None
reports = 0
drone_id = 1
try:
    while conn == None:
        try:
            conn = db_connect()
        except:
            sleep(1)
            continue
except:
    pass

cap = cv2.VideoCapture(1)
i = 0
while True:
    if i == 120:
        i = 0
        rails_detected = False
        _, frame = cap.read()
        original = frame.copy()
        edited, resized = edit_simple(original)
        try:
            rails_org = frame.copy()
            l_x1, r_x1, xl, yl, xr, yr = detect_rails(edited, rails_org)
            rails_detected = True
        except UnboundLocalError:
            try:
                rails_org = frame.copy()
                edited_2, resized = edit_image(original)
                l_x1, r_x1, xl, yl, xr, yr = detect_rails(edited_2, rails_org)
                rails_detected = True
            except:
                i = 120
                continue

        if rails_detected:
            if (rails_anomaly(rails_org, original)):
                img_yolo = anomaly_classification(original.copy())
                cv2.imwrite(f"report_photos/{drone_id}_{reports}.jpg", img_yolo)
                report_obstacle(conn, drone_id, reports, 3)
                reports += 1
            else:
                continue

    else:
        i += 1
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
conn.close()