import cv2
import numpy as np

img = cv2.imread("Imgs/cards.jpg")
if img is None:
    print("Error: Unable to open image file.")
    exit()

pts1 = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250], [250, 250]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (300, 300))

cv2.imshow("Original", img)
cv2.imshow("Transformed", result)
cv2.waitKey(0)
cv2.destroyAllWindows()