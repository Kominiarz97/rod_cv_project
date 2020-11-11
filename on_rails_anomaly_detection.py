import cv2
import numpy as np


def rails_mask(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    return mask

def rails_area(img):
    area = 0.0
    hsv_img_crop = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 200])
    upper_white = np.array([255, 80, 255])
    mask = cv2.inRange(hsv_img_crop, lower_white, upper_white)
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    for contour in contours:
        area += cv2.contourArea(contour)
    return area

def rails_anomaly(image, original, railway_type):
    mask=rails_mask(image.copy())
    rails = cv2.bitwise_and(original.copy(), original.copy(), mask=mask)
    _, h, _ = rails.shape
    print(rails_area(rails[int(h/2):h,:]))
    if rails_area(rails[int(h/2):h,:])<20000:
        return True
    else:
        return False



