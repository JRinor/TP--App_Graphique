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

cv2.imshow("Original", cv2.resize(img, (400, 300)))
cv2.imshow("Gray", cv2.resize(imgGray, (400, 300)))
cv2.imshow("Noisy", cv2.resize(imgNoisy, (400, 300)))
cv2.imshow("Canny", cv2.resize(imgCanny, (400, 300)))
cv2.imshow("Dilation", cv2.resize(imgDilation, (400, 300)))
cv2.imshow("Eroded", cv2.resize(imgEroded, (400, 300)))
cv2.imshow("Resized", cv2.resize(imgResize, (400, 300)))
cv2.imshow("Cropped", cv2.resize(imgCropped, (400, 300)))

cv2.waitKey(0)
cv2.destroyAllWindows()