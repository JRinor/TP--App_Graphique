import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (50, 50), (462, 462), (0, 0, 255), -1)
cv2.circle(img, (256, 256), 150, (255, 255, 255), -1)
cv2.putText(img, "INFO", (120, 260), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10)
cv2.putText(img, "DEPT", (180, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

cv2.imshow("Logo Departement INFO", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
