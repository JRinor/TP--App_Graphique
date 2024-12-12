import cv2 as cv

# Initialisation de la capture vidéo avec la caméra OBS
cap = cv.VideoCapture(1)  # Remplacez 1 par l'index correct de votre caméra OBS

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra OBS.")
    exit()

# Charger le classificateur Haar pour la détection des plaques d'immatriculation
plate_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_russian_plate_number.xml')

# Fonction pour détecter les plaques d'immatriculation
def detect_license_plates(frame):
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)  # Convertir l'image en niveaux de gris
    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(100, 50))  # Détecter les plaques
    return plates

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture vidéo")
        break

    # Détection des plaques d'immatriculation
    plates = detect_license_plates(frame)

    # Afficher les plaques détectées (rectangle autour des plaques)
    for (x, y, w, h) in plates:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Afficher l'image avec les plaques détectées
    cv.imshow('Détection de Plaques d\'Immatriculation', frame)

    # Quitter avec 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv.destroyAllWindows()
