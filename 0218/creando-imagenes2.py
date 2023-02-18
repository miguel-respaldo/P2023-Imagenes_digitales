import cv2 as cv
import numpy as np

img = np.zeros(shape=(500,500), dtype='uint8')

for filas in range(100):
    for columnas in range(100):
        img[filas][columnas] = 255

cv.imshow("Cuadro Negro", img)
k = cv.waitKey(0)

