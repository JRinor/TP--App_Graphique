import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

cv2.namedWindow("Selectionneur de couleur")

cv2.createTrackbar('H min', 'Selectionneur de couleur', 0, 179, nothing)
cv2.createTrackbar('S min', 'Selectionneur de couleur', 0, 255, nothing)
cv2.createTrackbar('V min', 'Selectionneur de couleur', 0, 255, nothing)
cv2.createTrackbar('H max', 'Selectionneur de couleur', 179, 179, nothing)
cv2.createTrackbar('S max', 'Selectionneur de couleur', 255, 255, nothing)
cv2.createTrackbar('V max', 'Selectionneur de couleur', 255, 255, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error during video capture.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('H min', 'Selectionneur de couleur')
    s_min = cv2.getTrackbarPos('S min', 'Selectionneur de couleur')
    v_min = cv2.getTrackbarPos('V min', 'Selectionneur de couleur')
    h_max = cv2.getTrackbarPos('H max', 'Selectionneur de couleur')
    s_max = cv2.getTrackbarPos('S max', 'Selectionneur de couleur')
    v_max = cv2.getTrackbarPos('V max', 'Selectionneur de couleur')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Segmentation Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
