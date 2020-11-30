import cv2
import imutils
import numpy as np
from rails_detection import draw_rails
image= cv2.imread(f"media/8.JPG")
image = imutils.resize(image, 400, 600)
cla = cv2.createCLAHE(clipLimit=25)
H, S, V = cv2.split(cv2.cvtColor(image, cv2.COLOR_BGR2HSV))
eq_V = cla.apply(V)
eq_image = cv2.cvtColor(cv2.merge([H, S, eq_V]), cv2.COLOR_HSV2BGR)
gray = cv2.cvtColor(eq_image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 180, 255)
cv2.imshow("imaaage",edges)
kernel = np.ones((3, 3), np.uint8)
dilate = cv2.dilate(edges, kernel, iterations=1)
erode = cv2.erode(dilate, kernel, iterations=1)
cv2.imshow("imaage",erode)
lines = cv2.HoughLinesP(erode, 1, np.pi/180, 80, minLineLength = 150, maxLineGap = 10)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if x2-x1 < 100:
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 5)
            draw_rails(image,x1,x2,y1,y2)
cv2.imshow("image",image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()



'''blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
edges = cv2.Canny(blur, 180, 255)
imga = imutils.resize(edges, 800, 1200)
cv2.imshow("imaage",imga)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 80, minLineLength = 1500, maxLineGap = 100)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 20)'''