import cv2 as cv
import numpy as np

def get_contours(img, imgContour):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 500:
            cv.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 2)
            if len(approx) == 3:
                cv.putText(imgContour, "Triangle", (x + w // 2 - 50, y + h // 2), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
            elif len(approx) == 4:
                cv.putText(imgContour, "Rectangle", (x + w // 2 - 60, y + h // 2), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
            elif len(approx) > 4:
                cv.putText(imgContour, "Circle", (x + w // 2 - 40, y + h // 2), cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)
image_path = 'imgs/shapes.png'
frame = cv.imread(image_path)

if frame is None:
    print("Erreur de chargement de l'image")
    exit()
frame = cv.resize(frame, (600, 400))
imgContour = frame.copy()
imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)
get_contours(imgCanny, imgContour)
cv.imshow("Image Originale", frame)
cv.imshow("Contours", imgContour)
cv.imshow("Canny", imgCanny)
cv.waitKey(0)
cv.destroyAllWindows()
