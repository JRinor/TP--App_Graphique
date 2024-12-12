import cv2
import numpy as np

def nothing(x):
    pass

drawing = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Paint')

cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)
cv2.createTrackbar('Radius', 'Paint', 1, 20, nothing)

drawing_mode = False
last_point = (-1, -1)

def draw(event, x, y, flags, param):
    global drawing_mode, last_point
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_mode = True
        last_point = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and drawing_mode:
        r = cv2.getTrackbarPos('R', 'Paint')
        g = cv2.getTrackbarPos('G', 'Paint')
        b = cv2.getTrackbarPos('B', 'Paint')
        radius = cv2.getTrackbarPos('Radius', 'Paint')
        cv2.line(drawing, last_point, (x, y), (b, g, r), radius * 2)
        last_point = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing_mode = False

cv2.setMouseCallback('Paint', draw)

while True:
    cv2.imshow('Paint', drawing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
