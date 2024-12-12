import cv2 as cv

# Charger l'image
img = cv.imread('imgs/visages.jpg')  # Remplacez par le chemin de votre image

# Charger le fichier XML du classificateur Haar pour la détection de visages
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Fonction de détection de visages
def detect_faces(img):
    # Convertir l'image en niveaux de gris
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Appliquer la détection de visages
    faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)

    # Dessiner des rectangles autour des visages détectés
    for (x, y, w, h) in faces_rect:
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Rectangle vert autour du visage

    return img

# Appliquer la détection de visages sur l'image
image_with_faces = detect_faces(img)

# Afficher l'image avec les visages détectés
cv.imshow("Détection de Visages", image_with_faces)

# Enregistrer l'image avec les rectangles autour des visages
cv.imwrite('image_detected_faces.jpg', image_with_faces)

# Attendre une touche pour fermer la fenêtre
cv.waitKey(0)

# Fermer les fenêtres OpenCV
cv.destroyAllWindows()
