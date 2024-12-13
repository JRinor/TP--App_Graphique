import cv2 as cv
img = cv.imread('imgs/visages.jpg')
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_faces(img):
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)
    for (x, y, w, h) in faces_rect:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    return img
image_with_faces = detect_faces(img)
cv.imshow("Détection de Visages", image_with_faces)
cv.imwrite('image_detected_faces.jpg', image_with_faces)
cv.waitKey(0)
cv.destroyAllWindows()
