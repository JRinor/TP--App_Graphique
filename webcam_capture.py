import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 20)

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()