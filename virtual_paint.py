import cv2
import numpy as np

def nothing(x):
    pass

# Create a window for trackbars
cv2.namedWindow("Trackbars")
cv2.createTrackbar("H Min", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("S Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("V Min", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("H Max", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("S Max", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("V Max", "Trackbars", 255, 255, nothing)

cap = cv2.VideoCapture(0)
drawing = np.zeros((480, 640, 3), np.uint8)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("H Min", "Trackbars")
    s_min = cv2.getTrackbarPos("S Min", "Trackbars")
    v_min = cv2.getTrackbarPos("V Min", "Trackbars")
    h_max = cv2.getTrackbarPos("H Max", "Trackbars")
    s_max = cv2.getTrackbarPos("S Max", "Trackbars")
    v_max = cv2.getTrackbarPos("V Max", "Trackbars")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(drawing, (x + w // 2, y + h // 2), 10, (0, 0, 255), -1)

    combined = cv2.addWeighted(frame, 0.5, drawing, 0.5, 0)
    cv2.imshow("Virtual Paint", combined)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()