import cv2
import imutils
import numpy as np


def edit_simple(image):
    resized = imutils.resize(image.copy(), 400, 600)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 120, 255)
    cv2.imshow("aaaaaas", edges)
    return edges, resized


def edit_image(image):
    resized = imutils.resize(image.copy(), 400, 600)
    cla = cv2.createCLAHE(clipLimit=4.0)
    H, S, V = cv2.split(cv2.cvtColor(resized.copy(), cv2.COLOR_BGR2HSV))
    eq_V = cla.apply(V)
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(eq_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 120, 255)
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(edges, kernel, iterations=1)
    erode = cv2.erode(dilate, kernel, iterations=1)
    return erode, resized


def edit_dist(image):
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    cv2.normalize(dist, dist, 1, 0, cv2.NORM_INF)
    _, final = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY_INV)
    return final
