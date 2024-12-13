import cv2 as cv
import numpy as np
image_path = 'imgs/img_perspective.jpg'
image = cv.imread(image_path)
def find_document_contour(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blurred, 100, 200)
    dilated = cv.dilate(edges, None, iterations=2)
    contours, _ = cv.findContours(dilated, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    largest_contour = max(contours, key=cv.contourArea)
    return largest_contour
def get_document_points(contour):
    peri = cv.arcLength(contour, True)
    approx = cv.approxPolyDP(contour, 0.02 * peri, True)
    if len(approx) == 4:
        return approx
    return None
def transform_perspective(img, points):
    points = sorted(points, key=lambda x: x[0][0])
    left_points = sorted(points[:2], key=lambda x: x[0][1])
    right_points = sorted(points[2:], key=lambda x: x[0][1])

    sorted_points = np.array(left_points + right_points, dtype="float32")
    width, height = 500, 700
    dst_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
    matrix = cv.getPerspectiveTransform(sorted_points, dst_points)
    result = cv.warpPerspective(img, matrix, (width, height))
    return result
document_contour = find_document_contour(image)
document_points = get_document_points(document_contour)
if document_points is not None:
    for point in document_points:
        cv.circle(image, tuple(point[0]), 10, (0, 255, 0), -1)
    cv.polylines(image, [document_points], isClosed=True, color=(0, 255, 0), thickness=2)
    result_image = transform_perspective(image, document_points)
    cv.imshow("Image Originale avec Sélection", image)
    cv.imshow("Document Scanné", result_image)

    cv.waitKey(0)
    cv.destroyAllWindows()
else:
    print("Aucun document détecté.")
