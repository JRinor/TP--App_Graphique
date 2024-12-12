# Rapport de TP : Application Graphique avec OpenCV

## Introduction
Ce TP m'a permis d'approfondir mes connaissances en traitement d'images et de vidéos avec OpenCV, une bibliothèque puissante pour la vision par ordinateur. OpenCV (Open Source Computer Vision Library) est une bibliothèque open-source qui contient plus de 2500 algorithmes optimisés pour la vision par ordinateur et l'apprentissage automatique. Elle est largement utilisée pour des applications telles que la détection d'objets, la reconnaissance faciale, la segmentation d'images, et bien plus encore. Pour ce TP, j'ai également utilisé des bibliothèques complémentaires comme **numpy** pour la manipulation de tableaux et **matplotlib** pour la visualisation des données.

---

## Objectifs du TP
- Apprendre les bases de la manipulation d'images et de vidéos.
- Explorer les fonctionnalités avancées d'OpenCV telles que la segmentation de couleurs et la transformation de perspective.
- Utiliser des algorithmes de détection d'objets pour analyser des images.
- Créer des applications interactives utilisant des événements souris et des barres de réglage.

---

Voici une partie à ajouter à votre README pour expliquer comment créer et configurer le projet avec Git, l'environnement virtuel, et OpenCV.

---

## Installation et Configuration du Projet

### 1. Cloner le Dépôt
Pour commencer, vous devez cloner ce projet à partir de GitHub. Utilisez la commande suivante dans votre terminal ou ligne de commande pour récupérer les fichiers du projet :

```bash
git clone <URL_du_dépôt>
cd TP--App_Graphique
```

### 2. Créer et Activer un Environnement Virtuel

#### Sur Windows
1. Créez un environnement virtuel avec la commande suivante :
   
   ```bash
   python -m venv-windows venv-windows
   ```

2. Activez l'environnement virtuel en exécutant le script d'activation dans le dossier `venv/Scripts/` :

   ```bash
   .\venv\Scripts\activate
   ```

   Vous devriez voir le nom de l'environnement virtuel (par exemple `(venv)`) dans votre invite de commande, ce qui indique que l'environnement est activé.

#### Sur Linux ou macOS
1. Créez un environnement virtuel avec la commande suivante :
   
   ```bash
   python3 -m venv-windows venv-windows
   ```

2. Activez l'environnement virtuel avec cette commande :

   ```bash
   source venv-windows/bin/activate
   ```

   Vous devriez voir le nom de l'environnement virtuel (par exemple `(venv)`) dans votre terminal, ce qui signifie que l'environnement est activé.

### 3. Installer les Dépendances

Une fois que votre environnement virtuel est activé, vous devez installer les dépendances du projet. Le principal paquet requis est OpenCV, que vous pouvez installer avec `pip` :

```bash
pip install opencv-python
```

Cela installera la bibliothèque OpenCV et toutes ses dépendances nécessaires pour exécuter les scripts du projet.

---
## Arborescence du Projet

```
TP--App_Graphique
├── imgs
│   ├── 1.jpg
│   ├── car.png
│   ├── cards.jpg
│   ├── contours.pgm
│   ├── img_perspective.jpg
│   ├── lena.png
│   ├── lenaBis.png
│   ├── shapes.png
│   ├── tigre.jpg
│   └── visages.jpg
├── exo1.py
├── exo2.py
├── exo3.py
├── color_segmentation.py
├── document_scanner_camera.py
├── document_scanner_image.py
├── draw_shapes.py
├── face_detection.py
├── geometric_object_detection.py
├── image_processing.py
├── Install-OpenCV.py
├── load_register_img.py
├── mouse_events.py
├── perspective_transformation.py
├── radar_application.py
├── trackbars.py
├── video_display.py
├── virtual_paint.py
└── webcam_capture.py
```

---

### Scripts Python
Voici la liste complète des scripts Python créés pour ce TP :

| Nom du fichier                 | Description                                         |
|--------------------------------|-----------------------------------------------------|
| `exo1.py`                      | Introduction aux bases d'OpenCV.                    |
| `exo2.py`                      | Approfondissement des manipulations d'images.       |
| `exo3.py`                      | Applications avancées et transformation.            |
| `color_segmentation.py`        | Segmentation de couleurs dans une image.            |
| `document_scanner_camera.py`   | Scanner de documents à partir de la caméra.         |
| `document_scanner_image.py`    | Scanner de documents à partir d'une image.          |
| `draw_shapes.py`               | Dessin de formes géométriques simples.              |
| `face_detection.py`            | Détection de visages dans une image.                |
| `geometric_object_detection.py`| Détection d'objets géométriques.                    |
| `image_processing.py`          | Traitement d'images avec OpenCV.                    |
| `Install-OpenCV.py`            | Permet de vérifier la bonne installation de Open-Cv |
| `load_register_img.py`         | Chargement et alignement d'images.                  |
| `mouse_events.py`              | Interaction avec la souris.                         |
| `perspective_transformation.py`| Transformation de perspective.                      |
| `radar_application.py`         | Application radar simulée avec OpenCV.              |
| `trackbars.py`                 | Utilisation de barres de réglage interactives.      |
| `video_display.py`             | Lecture et affichage de vidéos.                     |
| `virtual_paint.py`             | Application interactive de peinture virtuelle.      |
| `webcam_capture.py`            | Capture vidéo depuis une webcam.                    |

---

## Description des Exercices

### Exercice 1 : Création d'un Logo avec des Formes Géométriques (`exo1.py`)
- **Objectif :** Créer une image contenant des formes géométriques et du texte.
- **Réalisation :**
  - Utilisation de `cv2.rectangle()`, `cv2.circle()` et `cv2.ellipse()` pour dessiner des formes.
  - Ajout de texte avec `cv2.putText()`.
  - Affichage de l'image finale avec `cv2.imshow()`.

```python
img = np.zeros((512, 512, 3), np.uint8)

cv2.rectangle(img, (50, 50), (462, 462), (0, 0, 255), -1)
cv2.circle(img, (256, 256), 150, (255, 255, 255), -1)
cv2.ellipse(img, (256, 256), (200, 100), 0, 0, 360, (255, 0, 0), -1)
cv2.putText(img, "INFO", (120, 260), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 255, 255), 10)
cv2.putText(img, "DEPT", (180, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
cv2.putText(img, "UNIVERSITY", (100, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Logo Departement INFO", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Exercice 2 : Application de Peinture Interactive (`exo2.py`)
- **Objectif :** Créer une application interactive permettant de dessiner avec des couleurs et des tailles de pinceau ajustables.
- **Réalisation :**
  - Utilisation des barres de réglage (`cv2.createTrackbar()`) pour sélectionner les couleurs et la taille du pinceau.
  - Gestion des événements souris avec `cv2.EVENT_LBUTTONDOWN`, `cv2.EVENT_MOUSEMOVE` et `cv2.EVENT_LBUTTONUP`.
  - Dessin de cercles sur l'image en fonction de la position de la souris.

```python
def nothing(x):
    pass

drawing = np.full((512, 512, 3), 200, np.uint8)
cv2.namedWindow('Paint')

cv2.createTrackbar('R', 'Paint', 0, 255, nothing)
cv2.createTrackbar('G', 'Paint', 0, 255, nothing)
cv2.createTrackbar('B', 'Paint', 0, 255, nothing)
cv2.createTrackbar('Radius', 'Paint', 1, 20, nothing)

def draw(event, x, y, flags, param):
    global drawing_mode
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_mode = True
    elif event == cv2.EVENT_MOUSEMOVE and drawing_mode:
        r = cv2.getTrackbarPos('R', 'Paint')
        g = cv2.getTrackbarPos('G', 'Paint')
        b = cv2.getTrackbarPos('B', 'Paint')
        radius = cv2.getTrackbarPos('Radius', 'Paint')
        cv2.circle(drawing, (x, y), radius, (b, g, r), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing_mode = False

cv2.setMouseCallback('Paint', draw)

while True:
    cv2.imshow('Paint', drawing)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
```

### Exercice 3 : Segmentation de Couleurs en Temps Réel (`exo3.py`)
- **Objectif :** Isoler des objets dans une vidéo en fonction de leur couleur.
- **Réalisation :**
  - Capture vidéo en temps réel avec `cv2.VideoCapture()`.
  - Utilisation de l'espace HSV pour définir des plages de couleurs à segmenter.
  - Création de masques binaires pour isoler les couleurs cibles et application de ces masques sur la vidéo.

```python
def nothing(x):
    pass

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

cv2.namedWindow("Selectionneur de couleur")

cv2.createTrackbar('H min', 'Selectionneur de couleur', 0, 179, nothing)
cv2.createTrackbar('S min', 'Selectionneur de couleur', 0, 255, nothing)
cv2.createTrackbar('V min', 'Selectionneur de couleur', 0, 255, nothing)
cv2.createTrackbar('H max', 'Selectionneur de couleur', 179, 179, nothing)
cv2.createTrackbar('S max', 'Selectionneur de couleur', 255, 255, nothing)
cv2.createTrackbar('V max', 'Selectionneur de couleur', 255, 255, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error during video capture.")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos('H min', 'Selectionneur de couleur')
    s_min = cv2.getTrackbarPos('S min', 'Selectionneur de couleur')
    v_min = cv2.getTrackbarPos('V min', 'Selectionneur de couleur')
    h_max = cv2.getTrackbarPos('H max', 'Selectionneur de couleur')
    s_max = cv2.getTrackbarPos('S max', 'Selectionneur de couleur')
    v_max = cv2.getTrackbarPos('V max', 'Selectionneur de couleur')

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original', frame)
    cv2.imshow('Segmentation Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

