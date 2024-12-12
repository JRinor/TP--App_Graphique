import cv2 as cv
import numpy as np

# Fonction pour trouver le contour du document
def find_document_contour(img):
    # Convertir en niveaux de gris et égaliser l'histogramme pour améliorer le contraste
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)

    # Appliquer un flou gaussien pour réduire le bruit
    blurred = cv.GaussianBlur(gray, (5, 5), 0)

    # Appliquer Canny pour détecter les bords
    edges = cv.Canny(blurred, 50, 150)

    # Appliquer une dilatation pour renforcer les contours détectés
    dilated = cv.dilate(edges, None, iterations=2)

    # Trouver les contours
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        # Trouver le contour ayant la plus grande aire
        largest_contour = max(contours, key=cv.contourArea)
        return largest_contour
    return None

# Fonction pour obtenir les 4 coins du document
def get_document_points(contour):
    peri = cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, 0.02 * peri, True)
    if len(approx) == 4:
        return approx
    return None

# Fonction pour transformer la perspective de l'image
def transform_perspective(img, points):
    # Trier les points pour obtenir [haut-gauche, haut-droit, bas-gauche, bas-droit]
    points = sorted(points, key=lambda x: x[0][0])  # Trier par coordonnée x
    left_points = sorted(points[:2], key=lambda x: x[0][1])  # Trier les points à gauche par coordonnée y
    right_points = sorted(points[2:], key=lambda x: x[0][1])  # Trier les points à droite par coordonnée y

    sorted_points = np.array(left_points + right_points, dtype="float32")

    # Définir la taille du document de sortie
    width, height = 500, 700  # Ajustez en fonction de l'image du document
    dst_points = np.float32([[0, 0], [width-1, 0], [0, height-1], [width-1, height-1]])

    # Obtenir la matrice de transformation de perspective
    matrix = cv.getPerspectiveTransform(sorted_points, dst_points)

    # Appliquer la transformation de perspective
    result = cv.warpPerspective(img, matrix, (width, height))
    return result

# Initialisation de la capture vidéo avec la caméra OBS
cap = cv.VideoCapture(1)  # Remplacez par l'index correct de votre caméra OBS (0 est souvent la webcam par défaut)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra OBS.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture vidéo")
        break

    # Trouver le contour du document
    document_contour = find_document_contour(frame)

    # Si le contour du document est trouvé
    if document_contour is not None:
        # Récupérer les 4 coins du document
        document_points = get_document_points(document_contour)

        if document_points is not None:
            # Afficher les points sélectionnés sur l'image originale
            for point in document_points:
                cv.circle(frame, tuple(point[0]), 10, (0, 255, 0), -1)  # Cercle vert pour les points

            # Relier les points pour afficher le contour du document
            cv.polylines(frame, [document_points], isClosed=True, color=(0, 255, 0), thickness=2)

            # Appliquer la transformation de perspective
            result_image = transform_perspective(frame, document_points)

            # Afficher l'image transformée
            cv.imshow("Document Scanné", result_image)

    # Afficher l'image originale avec le contour du document
    cv.imshow("Image Originale", frame)

    # Quitter la boucle avec la touche 'q'
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et fermer les fenêtres
cap.release()
cv.destroyAllWindows()
