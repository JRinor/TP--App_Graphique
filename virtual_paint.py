import cv2
import numpy as np


# Fonction pour détecter la couleur bleue du capuchon
def detect_blue_capuchon(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Plage de couleur pour détecter le bleu
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    return mask


def virtual_paint():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Erreur d'ouverture de la caméra")
        return

    last_x, last_y = -1, -1  # Dernière position du capuchon
    canvas = None  # Canvas pour dessiner

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erreur de lecture de la caméra")
            break

        # Si c'est la première image, créer un "canvas" vide pour dessiner dessus
        if canvas is None:
            canvas = np.zeros_like(frame)

        # Détection du capuchon bleu
        mask = detect_blue_capuchon(frame)
        # Améliorer la détection avec un flou et contour
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            # Chercher le plus grand contour
            max_contour = max(contours, key=cv2.contourArea)
            (x, y, w, h) = cv2.boundingRect(max_contour)

            # Si la taille du capuchon est suffisante, on dessine
            if w > 30 and h > 30:
                # Position du centre du capuchon
                cap_position = (x + w // 2, y + h // 2)

                # Si la dernière position est définie et que le capuchon est en mouvement, dessiner
                if last_x != -1 and last_y != -1:
                    # Dessiner la ligne sur le "canvas" pour ne pas la supprimer
                    cv2.line(canvas, (last_x, last_y), cap_position, (0, 0, 255), 5)

                # Dessiner le capuchon détecté sur l'image de la caméra
                cv2.circle(frame, cap_position, 10, (0, 0, 255), -1)  # Cercle rouge sur le capuchon

                last_x, last_y = cap_position  # Mettre à jour la dernière position du capuchon

        # Fusionner le "canvas" avec l'image de la caméra pour afficher les lignes permanentes
        result = cv2.add(frame, canvas)

        # Affichage de la frame avec le dessin
        cv2.imshow("Virtual Paint", result)

        # Gestion des commandes
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Quitter l'application
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    virtual_paint()
