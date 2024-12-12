import cv2
import numpy as np

img = cv2.imread("Imgs/shapes.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

imgContour = img.copy()
for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255, 0, 0), 3)
    x, y, w, h = cv2.boundingRect(cnt)
    center, radius = cv2.minEnclosingCircle(cnt)
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
    print(len(approx))
    cv2.putText(imgContour, "objet", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0), 2)

cv2.imshow("Original", img)
cv2.imshow("Contours", imgContour)
cv2.waitKey(0)
cv2.destroyAllWindows()