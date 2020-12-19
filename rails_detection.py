import cv2
import numpy as np
import imutils

def detect_rails(edited, original): #funkcja przyjmuje jako parametry przetworzony obraz, oraz oryginalny obraz
    lines = cv2.HoughLinesP(edited, 1, np.pi/180, 80, minLineLength = 50, maxLineGap = 30)#detekcja linii prostych
    h, w, _ = original.shape #odczytanie wymiarów obrazu wejściowego
    ratio = int(h/600)
    l_x1 = int(w/2) #wydzielenie środka obrazu
    r_x1 = 0
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if x2 - x1 < 80: #ograniczenie do linii pionowych i z niewielką odchyłką
                if x1 < l_x1 and y1>550: #detekcja lewej szyny
                    l_x1, l_y1, l_x2, l_y2 = line[0]
                if x1 > r_x1 and y1>550:#detekcja prawej szyny
                    r_x1, r_y1, r_x2, r_y2 = line[0]
                if x2 > r_x1 and y2>550:
                    r_x2, r_y2, r_x1, r_y1 = line[0]
        # rysowanie linii szyn
        xl, yl = draw_rails(original, l_x1 * ratio, (l_x2 * ratio) + 25, l_y1 * ratio, l_y2 * ratio, 120)
        xr, yr = draw_rails(original, r_x1 * ratio, (r_x2 * ratio) - 25, r_y1 * ratio, r_y2 * ratio, 120)
    return l_x1 * ratio, r_x1 * ratio, xl, yl, xr, yr #funkcja zwraca położenie szyn


def draw_rails(img, x1, x2, y1, y2, thickness):
    h, _, _=img.shape
    l = int(h/2)
    #obliczenie kąta szyn
    theta = np.arctan2(y1 - y2, x1 - x2)
    x = int(x1 - l * np.cos(theta))
    y = int(y1 - l * np.sin(theta))
    #rysowanie linii wzdłuż szyn
    cv2.line(img, (x1, h), (x, y), (255,0,0), thickness)
    return x, y

'''img_1=orginal.copy()
        xl, yl=draw_rails(orginal, l_x1 * 10, (l_x2 * 10) + 25, l_y1 * 10, l_y2 * 10)
        xr, yr=draw_rails(orginal, r_x1 * 10, (r_x2 * 10) - 25, r_y1 * 10, r_y2 * 10)
        draw_rectangles(img_1, l_x1 * 10, (l_x2 * 10) + 25, l_y1 * 10, l_y2 * 10)
        draw_rectangles(img_1, r_x1 * 10, (r_x2 * 10) - 25, r_y1 * 10, r_y2 * 10)
    return img_1, l_x1, r_x1, xl, yl, xr, yr

def draw_rails(img, x1, x2, y1, y2):
    h,_,_=img.shape
    if x1-x2<0:
        theta = np.arctan2(y1 - y2, x1 - x2)
    else:
        theta = np.arctan2(y1 - y2, x1 - x2)
    x = int(x1 - 5000 * np.cos(theta))
    y = int(y1 - 5000 * np.sin(theta))
    cv2.line(img, (x1, h), (x, y), (255,0,0), 120)
    return x,y'''