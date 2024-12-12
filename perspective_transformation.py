import cv2 as cv
import numpy as np

# Liste pour stocker les points de clics
points = []


# Fonction pour capturer les points de la souris et afficher les coordonnées
def click_event(event, x, y, flags, param):
    global points
    if event == cv.EVENT_LBUTTONDOWN:
        # Ajouter le point cliqué à la liste
        points.append((x, y))

        # Marquer le point avec un cercle rouge
        cv.circle(frame, (x, y), 5, (0, 0, 255), -1)

        # Afficher les coordonnées du point sur l'image
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, f"({x}, {y})", (x + 10, y - 10), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)

        # Actualiser l'affichage
        cv.imshow("Image", frame)

        # Lorsque 4 points ont été sélectionnés
        if len(points) == 4:
            # Définir les points de sortie (où l'image sera transformée)
            width, height = 500, 500  # Dimensions de l'image de sortie
            pts1 = np.float32(points)  # Points d'entrée (points sélectionnés sur l'image)

            # Points de destination : coins de l'image transformée
            pts2 = np.float32(
                [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])  # Coins de la nouvelle image

            # Obtenir la matrice de transformation de perspective
            matrix = cv.getPerspectiveTransform(pts1, pts2)

            # Appliquer la transformation de perspective
            transformed_img = cv.warpPerspective(frame, matrix, (width, height))

            # Afficher l'image transformée
            cv.imshow("Transformed Image", transformed_img)

            # Sauvegarder l'image transformée
            cv.imwrite('transformed_image.jpg', transformed_img)


# Charger l'image à transformer
image_path = 'imgs/cards.jpg'  # Remplace ce chemin par le chemin de ton image
frame = cv.imread(image_path)

if frame is None:
    print("Erreur de chargement de l'image")
    exit()

# Afficher l'image et attendre que l'utilisateur clique sur 4 points
cv.imshow("Image", frame)

# Attendre 4 clics de souris pour sélectionner les points
cv.setMouseCallback("Image", click_event)

# Attente jusqu'à ce que l'utilisateur ferme la fenêtre
cv.waitKey(0)
cv.destroyAllWindows()
