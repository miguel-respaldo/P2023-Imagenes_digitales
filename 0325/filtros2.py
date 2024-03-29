#!/usr/bin/env python3
import cv2 as cv
import numpy as np

# Se lee la imagen
img = cv.imread("../imgs/persona.jpg")

assert img is not None, "file could not be read, check with os.path.exists()"

# Obtenemos su forma
fil, col, ch = img.shape

escalar = 1
#escalar = 1/3

Dx = escalar * np.array([
          [-1.,  0.,  1.],
          [-1.,  0.,  1.],
          [-1.,  0.,  1.]])

Dy = escalar * np.array([
          [-1., -1., -1.],
          [ 0.,  0.,  0.],
          [ 1.,  1.,  1.]])

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

img_dx = cv.filter2D(img_gray, -1, Dx)
img_dy = cv.filter2D(img_gray, -1, Dy)
img_Lap = np.absolute(img_dx) + np.absolute(img_dy)

cv.imshow("Original", img_gray)
cv.imshow("Filtrada Dx", img_dx)
cv.imshow("Filtrada Dy", img_dy)
cv.imshow("Filtrada Laplaciano", img_Lap)

while True:
    # Leemos del teclado
    key = cv.waitKey(1000)
    # Verificamos si la ventana es visible
    win =  cv.getWindowProperty('Original', cv.WND_PROP_VISIBLE)

    # si se preciona la tecla ESC
    if key == 27 or key == ord("q") or win < 1.0:
        break

cv.destroyAllWindows()

