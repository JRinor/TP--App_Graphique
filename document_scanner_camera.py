import cv2 as cv
import numpy as np
def find_document_contour(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    gray = cv.equalizeHist(gray)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    edges = cv.Canny(blurred, 50, 150)
    dilated = cv.dilate(edges, None, iterations=2)
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv.contourArea)
        return largest_contour
    return None
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
    dst_points = np.float32([[0, 0], [width-1, 0], [0, height-1], [width-1, height-1]])
    matrix = cv.getPerspectiveTransform(sorted_points, dst_points)
    result = cv.warpPerspective(img, matrix, (width, height))
    return result
cap = cv.VideoCapture(1)

if not cap.isOpened():
    print("Erreur : Impossible d'ouvrir la caméra OBS.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture vidéo")
        break
    document_contour = find_document_contour(frame)
    if document_contour is not None:
        document_points = get_document_points(document_contour)

        if document_points is not None:
            for point in document_points:
                cv.circle(frame, tuple(point[0]), 10, (0, 255, 0), -1)
            cv.polylines(frame, [document_points], isClosed=True, color=(0, 255, 0), thickness=2)
            result_image = transform_perspective(frame, document_points)
            cv.imshow("Document Scanné", result_image)
    cv.imshow("Image Originale", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()
