import cv2
import numpy as np

mode = True


def draw_shape(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:
        if mode:

            cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
        else:

            cv2.rectangle(img, (x - 10, y - 10), (x + 10, y + 10), (0, 255, 0), -1)


# Crée une image noire
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')

cv2.setMouseCallback('image', draw_shape)

print("Appuyez sur 'm' pour changer de mode (cercle/rectangle).")
print("Appuyez sur 'q' pour quitter.")

while True:
    cv2.imshow('image', img)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break
    elif key == ord('m'):
        mode = not mode
        print("Mode:", "Cercle" if mode else "Rectangle")

cv2.destroyAllWindows()
