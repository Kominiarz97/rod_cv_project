import cv2
import numpy as np
import imutils

def detect_rails(edited, original):
    lines = cv2.HoughLinesP(edited, 1, np.pi/180, 80, minLineLength = 50, maxLineGap = 30)
    _, h, w = original.shape
    ratio = int(h/600)
    l_x1 = 200
    r_x1 = 0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x1 < l_x1 and y1>550:
                l_x1 = x1
                l_x2 = x2
                l_y1 = y1
                l_y2 = y2
            if x1 > r_x1 and y1>550:
                r_x1 = x1
                r_x2 = x2
                r_y1 = y1
                r_y2 = y2
            if x2 > r_x1 and y2>550:
                r_x1 = x2
                r_x2 = x1
                r_y1 = y2
                r_y2 = y1
            #cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 50)
        xl, yl=draw_rails(original, l_x1 * ratio, (l_x2 * ratio) + 25, l_y1 * ratio, l_y2 * ratio)
        xr, yr=draw_rails(original, r_x1 * ratio, (r_x2 * ratio) - 25, r_y1 * ratio, r_y2 * ratio)
        imagensy = imutils.resize(original, 400, 600)
        cv2.imshow("3", imagensy)
    return l_x1, r_x1, xl, yl, xr, yr

def draw_rails(img, x1, x2, y1, y2):
    h,_,_=img.shape
    l = int(h/2)
    if x1-x2<0:
        theta = np.arctan2(y1 - y2, x1 - x2)
    else:
        theta = np.arctan2(y1 - y2, x2 - x1)
    x = int(x1 - l * np.cos(theta))
    y = int(y1 - l * np.sin(theta))
    cv2.line(img, (x1, h), (x, y), (255,0,0), 5)
    return x, y

