import cv2
import numpy as np


def rails_mask(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)#zmiana przestrzeni barw
    lower_blue = np.array([100, 150, 0])#dolny zakres koloru niebieskiego
    upper_blue = np.array([140, 255, 255])#górny zakres koloru niebieskiego
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)#stworzenie maski
    return mask


def rails_area(img):
    area = 0.0
    hsv_img_crop = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)#zmiana przestrzeni barw
    lower_white = np.array([0, 0, 200])#dolny zakres koloru białego
    upper_white = np.array([255, 80, 255])#górny zakres koloru białego
    mask = cv2.inRange(hsv_img_crop, lower_white, upper_white)#stworzenie maski
    #znalezienie konturów białych obszarów
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[0]
    for contour in contours:
        area += cv2.contourArea(contour)#obliczanie powierzchni białych obszarów
    return area

def rails_anomaly(image, original):
    mask = rails_mask(image.copy()) #stworzenie maski
    rails = cv2.bitwise_and(original.copy(), original.copy(), mask=mask) #nałożenie maski
    _, h, _ = rails.shape #wysokość obrazu
    # warunek sprawdzający czy liczba białych pikseli zgadza się
    # z wartością odpowiadającą torom bez przeszkód
    if rails_area(rails[int(h / 2):h, :]) < 20000:
        return True
    else:
        return False

