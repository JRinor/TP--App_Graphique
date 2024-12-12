import cv2

cap = cv2.VideoCapture("Imgs/sample-mp4-file.mp4")

while True:
    success, img = cap.read()
    if not success:
        break
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()