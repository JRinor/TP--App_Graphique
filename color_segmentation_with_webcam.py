import cv2 as cv
import numpy as np

def empty(a):
    pass

cap = cv.VideoCapture(0)

cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 800, 300)

cv.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture vidéo")
        break

    frame = cv.resize(frame, (600, 400))

    imgHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    h_min = cv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv.getTrackbarPos("Val Max", "Trackbars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv.inRange(imgHSV, lower, upper)

    imgResult = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("Image Originale", frame)
    cv.imshow("Image HSV", imgHSV)
    cv.imshow("Masque", mask)
    cv.imshow("Image Segmentee", imgResult)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
