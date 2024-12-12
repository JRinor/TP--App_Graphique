import cv2 as cv
import numpy as np

# Charger l'image
image_path = 'imgs/img_perspective.jpg'  # Remplacez ce chemin par le bon chemin
image = cv.imread(image_path)


# Fonction pour trouver le contour du document dans l'image
def find_document_contour(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blurred, 100, 200)
    dilated = cv.dilate(edges, None, iterations=2)
    contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv.contourArea)
    return largest_contour


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
    dst_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])

    # Obtenir la matrice de transformation de perspective
    matrix = cv.getPerspectiveTransform(sorted_points, dst_points)

    # Appliquer la transformation de perspective
    result = cv.warpPerspective(img, matrix, (width, height))
    return result


# Traitement de l'image
document_contour = find_document_contour(image)

# Récupérer les 4 coins du document
document_points = get_document_points(document_contour)

# Si les points sont valides, appliquer la transformation
if document_points is not None:
    # Afficher les points sélectionnés sur l'image originale
    for point in document_points:
        cv.circle(image, tuple(point[0]), 10, (0, 255, 0), -1)  # Cercle vert pour les points

    # Relier les points pour afficher le contour du document
    cv.polylines(image, [document_points], isClosed=True, color=(0, 255, 0), thickness=2)

    # Appliquer la transformation de perspective
    result_image = transform_perspective(image, document_points)

    # Afficher l'image originale avec la sélection
    cv.imshow("Image Originale avec Sélection", image)

    # Afficher l'image transformée
    cv.imshow("Document Scanné", result_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Aucun document détecté.")
