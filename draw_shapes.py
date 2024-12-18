import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
img[0:100, 0:100] = 255, 0, 0
cv2.line(img, (0, 0), (300, 200), (0, 0, 255), 3)
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
cv2.circle(img, (400, 50), 30, (255, 255, 0), cv2.FILLED)
cv2.putText(img, "TEST", (30, 200), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 150, 0), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()