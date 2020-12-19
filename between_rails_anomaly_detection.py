import cv2
import imutils
import numpy as np
from image_operations import edit_dist


def between_rails_anomaly(image, lx1, lx2, rx1, rx2):
    edited = edit_dist(image) #edycja obrazu
    mask = between_rails_mask(image, lx1, lx2, rx1, rx2)# stworzenie maski
    between_rails = cv2.bitwise_and(edited, edited, mask=mask)#nałożenie maski na obraz
    # warunek sprawdzający czy liczba niezerowych zgadza się
    # z wartością odpowiadającą obszarowi między szynami bez żadnych przeszkód
    if cv2.countNonZero(between_rails)<800000:
        return True
    else:
        return False


def between_rails_mask(image, lx1, lx2, rx1, rx2):
    h, w, _ = image.shape
    mask = np.zeros((h, w), dtype=np.uint8) #podstawa maski
    #macierz współrzędnych wierzchołków obszaru pomiędzy szynami kolejowymi
    pts = np.array([[lx1, h], [lx2, int(h / 2)], [rx2, int(h / 2)], [rx1, h]], np.int32)
    pts = pts.reshape((-1, 1, 2)) #przekształcenie macierzy punktów
    cv2.fillPoly(mask, [pts], 255) #wypełnienie obszaru białym kolorem
    return mask


