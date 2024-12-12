import cv2


img = cv2.imread("Imgs/lena.png")
cv2.imshow("in",img)
cv2.imwrite("Imgs/lenaBis.png", img)
cv2.waitKey(0)