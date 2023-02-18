import cv2 as cv
import numpy as np

img = np.zeros(shape=(256,256), dtype='uint8')

for filas in range(256):
    for columnas in range(256):
        img[filas][columnas] = columnas

cv.imshow("Degradado", img)
k = cv.waitKey(0)

