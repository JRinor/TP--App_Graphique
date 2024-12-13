import cv2 as cv
import numpy as np
points = []
def click_event(event, x, y, flags, param):
    global points
    if event == cv.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv.circle(frame, (x, y), 5, (0, 0, 255), -1)
        font = cv.FONT_HERSHEY_SIMPLEX
        cv.putText(frame, f"({x}, {y})", (x + 10, y - 10), font, 0.5, (0, 255, 0), 2, cv.LINE_AA)
        cv.imshow("Image", frame)
        if len(points) == 4:
            width, height = 500, 500
            pts1 = np.float32(points)
            pts2 = np.float32(
                [[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
            matrix = cv.getPerspectiveTransform(pts1, pts2)
            transformed_img = cv.warpPerspective(frame, matrix, (width, height))
            cv.imshow("Transformed Image", transformed_img)
            cv.imwrite('transformed_image.jpg', transformed_img)
image_path = 'imgs/cards.jpg'
frame = cv.imread(image_path)

if frame is None:
    print("Erreur de chargement de l'image")
    exit()
cv.imshow("Image", frame)
cv.setMouseCallback("Image", click_event)
cv.waitKey(0)
cv.destroyAllWindows()
