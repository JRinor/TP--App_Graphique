import cv2 as cv
cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra OBS.")
    exit()
plate_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_russian_plate_number.xml')
def detect_license_plates(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(100, 50))
    return plates

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture vidéo")
        break
    plates = detect_license_plates(frame)
    for (x, y, w, h) in plates:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('Détection de Plaques d\'Immatriculation', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
