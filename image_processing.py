import cv2
import numpy as np

img = cv2.imread("Imgs/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mean = 0
sigma = 25
gaussian_noise = np.random.normal(mean, sigma, imgGray.shape).astype(np.uint8)
imgNoisy = cv2.add(imgGray, gaussian_noise)
imgCanny = cv2.Canny(imgNoisy, 150, 200)
kernel = np.ones((5, 5), np.uint8)
imgDilation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDilation, kernel, iterations=1)
imgResize = cv2.resize(img, (1000, 500))
imgCropped = img[0:200, 100:300]

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Noisy", imgNoisy)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded", imgEroded)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCropped)

cv2.waitKey(0)
cv2.destroyAllWindows()