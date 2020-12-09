import cv2
import imutils
import numpy as np
from image_operations import edit_dist


def between_rails_anomaly(image, lx1, lx2, rx1, rx2):
    edited = edit_dist(image)
    mask = between_rails_mask(image, lx1, lx2, rx1, rx2)
    between_rails = cv2.bitwise_and(edited, edited, mask=mask)
    if area(between_rails)<800000:
        return True
    else:
        return False


def between_rails_mask(image, lx1, lx2, rx1, rx2):
    h, w, _ = image.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    pts = np.array([[lx1, h], [lx2, int(h / 2)], [rx2, int(h / 2)], [rx1, h]], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.fillPoly(mask, [pts], 255)
    return mask


def area(image):
    area = cv2.countNonZero(image)
    return area
