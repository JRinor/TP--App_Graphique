import cv2
import numpy as np


def detect_blue_capuchon(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask


def virtual_paint():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur d'ouverture de la caméra")
        return

    last_x, last_y = -1, -1
    canvas = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur de lecture de la caméra")
            break

        if canvas is None:
            canvas = np.zeros_like(frame)
        mask = detect_blue_capuchon(frame)
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(max_contour)
            if w > 30 and h > 30:
                cap_position = (x + w // 2, y + h // 2)
                if last_x != -1 and last_y != -1:
                    cv2.line(canvas, (last_x, last_y), cap_position, (0, 0, 255), 5)
                cv2.circle(frame, cap_position, 10, (0, 0, 255), -1)

                last_x, last_y = cap_position
        result = cv2.add(frame, canvas)
        cv2.imshow("Virtual Paint", result)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    virtual_paint()
