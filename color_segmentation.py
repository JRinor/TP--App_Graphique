import cv2 as cv
import numpy as np

def empty(a):
    pass

# Charger l'image
img = cv.imread('Imgs/car.png')  # Remplacez par le chemin de votre image
img = cv.resize(img, (600, 400))  # Redimensionner l'image pour une meilleure visualisation

# Créer une fenêtre pour les trackbars
cv.namedWindow("Trackbars")
cv.resizeWindow("Trackbars", 800, 300)

# Ajouter des trackbars pour H, S, et V min/max
cv.createTrackbar("Hue Min", "Trackbars", 0, 179, empty)
cv.createTrackbar("Hue Max", "Trackbars", 179, 179, empty)
cv.createTrackbar("Sat Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Sat Max", "Trackbars", 255, 255, empty)
cv.createTrackbar("Val Min", "Trackbars", 0, 255, empty)
cv.createTrackbar("Val Max", "Trackbars", 255, 255, empty)

while True:
    # Convertir l'image en espace HSV
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # Lire les valeurs des trackbars
    h_min = cv.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv.getTrackbarPos("Sat Min", "Trackbars")
    s_max = cv.getTrackbarPos("Sat Max", "Trackbars")
    v_min = cv.getTrackbarPos("Val Min", "Trackbars")
    v_max = cv.getTrackbarPos("Val Max", "Trackbars")

    # Créer les tableaux pour les limites inférieure et supérieure
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Créer le masque
    mask = cv.inRange(imgHSV, lower, upper)

    # Appliquer un AND logique entre l'image et le masque
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # Afficher les résultats
    cv.imshow("Image Originale", img)
    cv.imshow("Image HSV", imgHSV)
    cv.imshow("Masque", mask)
    cv.imshow("Image Segmentee", imgResult)

    # Quitter la boucle avec la touche 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Fermer toutes les fenêtres
cv.destroyAllWindows()