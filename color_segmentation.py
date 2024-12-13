import cv2 as cv
import numpy as np

def empty(a):
    pass

img = cv.imread('Imgs/car.png')
img = cv.resize(img, (600, 400))
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 800, 300)
cv.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv.getTrackbarPos("Val Max", "Trackbars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv.inRange(imgHSV, lower, upper)
    imgResult = cv.bitwise_and(img, img, mask=mask)
    cv.imshow("Image Originale", img)
    cv.imshow("Image HSV", imgHSV)
    cv.imshow("Masque", mask)
    cv.imshow("Image Segmentee", imgResult)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()