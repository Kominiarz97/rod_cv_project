import cv2
from time import sleep
from report import report_obstacle
from db_conn import db_connect
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import edit_simple, edit_image
from on_rails_anomaly_detection import rails_anomaly
from between_rails_anomaly_detection import between_rails_anomaly

reports = 0
drone_id = 1

conn = None
try:
    while conn is None:
        try:
            conn = db_connect()
        except:
            sleep(1)
            continue
except:
    pass

rails_detected = False
frame = cv2.imread(f"media/8.JPG")
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
        pass

if rails_detected:
    if rails_anomaly(rails_org, original) or between_rails_anomaly(original, l_x1, xl, r_x1, xr):
        img_yolo = anomaly_classification(original.copy())
        cv2.imwrite(f"report_photos/{drone_id}_{reports}.jpg", img_yolo)
        report_obstacle(conn, drone_id, reports, 3)
        reports += 1
    else:
        pass

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

conn.close()
