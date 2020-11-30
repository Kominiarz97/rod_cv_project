import cv2
import imutils
import numpy as np

'''def get_image(path):#image height:6000px width:4000px
    orginal = cv2.imread(path)
    h, w, _ = orginal.shape
    if w != 4000 or h != 6000:
        orginal = imutils.resize(orginal.copy(), 4000, 6000)
    resized = imutils.resize(orginal.copy(), 400, 600)
    edited = edit_image(resized)
    return orginal, resized, edited'''

def downsize(image):
    return imutils.resize(image.copy(), 400, 600)

def edit_image(image):
    resized = downsize(image)
    #cv2.imshow("1", resized)
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 120, 255)
    #cv2.imshow("2", edges)
    return edges, resized

def crop(image, left, right):
    h, w, _ = image.shape
    return image.copy()[(h/3):h,left-25:right+25]

def edit_dist(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    kernel = np.ones((3, 3), np.uint8)
    erode = cv2.erode(thresh, kernel, iterations=2)
    dilate = cv2.dilate(erode, kernel, iterations=2)
    dist = cv2.distanceTransform(dilate, cv2.DIST_L2, 5)
    cv2.normalize(dist, dist, 1, 0, cv2.NORM_INF)
    return dist