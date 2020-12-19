import cv2
import imutils
import numpy as np


def edit_simple(image):
    resized = imutils.resize(image.copy(), 400, 600)#zmiana rozdzielczości
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)#konwersja na skale szarości
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)#rozmycie
    edges = cv2.Canny(blur, 120, 255)#detekcja krawędzi
    return edges, resized


def edit_image(image):
    resized = imutils.resize(image.copy(), 400, 600)#zmiana rozdzielczości
    cla = cv2.createCLAHE(clipLimit=4.0)
    #wydzielenie 3 kanałów z obrazu
    H, S, V = cv2.split(cv2.cvtColor(resized.copy(), cv2.COLOR_BGR2HSV))
    #zwiększenie kontrastu
    eq_V = cla.apply(V)
    #połączenie kanałów
    eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
    gray = cv2.cvtColor(eq_image, cv2.COLOR_BGR2GRAY)#konwersja na skale szarości
    blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)#rozmycie
    edges = cv2.Canny(blur, 120, 255)#detekcja krawędzi
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv2.dilate(edges, kernel, iterations=1)#dylatacja krawędzi
    erode = cv2.erode(dilate, kernel, iterations=1)#erozja krawędzi
    return erode, resized


def edit_dist(image):
    gray = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2GRAY) #konwersja na skale szarości
    #progowanie
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5) #transformata odległościowa
    cv2.normalize(dist, dist, 1, 0, cv2.NORM_INF) #normalizacja onrazu
    _, final = cv2.threshold(dist, 0, 255, cv2.THRESH_BINARY_INV) #progowanie
    return final

