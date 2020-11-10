import cv2
import imutils

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
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
    edges = cv2.Canny(blur, 120, 255)
    return edges, resized

def crop(image, left, right):
    h, w, _ = image.shape
    return image.copy()[(h/3):h,left-25:right+25]