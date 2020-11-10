'''import cv2
import numpy as np
import imutils
from detect_obstacles import anomaly_classification
from rails_detection import detect_rails
from image_operations import get_image
from on_rails_anomaly_detection import rails_mask, rails_area, rails_anomaly
from gps import get_position


orginal, resized, edited=get_image('media/6.jpg')
orginal_2=orginal.copy()
bot_x1, bot_x2, _, _, _, _ = detect_rails(edited, orginal)
img=imutils.resize(orginal.copy(), 400, 600)
#img_crop_rails = img[200:600, bot_x1-25:bot_x2+25]
img_crop_rails = img[:,:]
mask = rails_mask(orginal)
rails = cv2.bitwise_and(orginal_2, orginal_2, mask=mask)

area = rails_area(rails[3000:6000, 0:])
print(area)



if rails_anomaly(area):
    img_yolo=anomaly_classification(orginal_2.copy())
    cv2.putText(img_yolo, "Wykryto anomalie", (60, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('YOLO',img_yolo)
else:
    cv2.putText(resized, "Nie wykryto anomalii", (30, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)

#final=imutils.resize(rails,400,600)[200:600, bot_x1-25:bot_x2+25]
get_position()
cv2.imshow('Resized image', resized)
cv2.imshow('Lines', img_crop_rails)
cv2.imshow('RAILS RAILS',resized)
cv2.waitKey(0)
cv2.destroyAllWindows()'''