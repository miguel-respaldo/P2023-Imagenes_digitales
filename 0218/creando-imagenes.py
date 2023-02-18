import cv2 as cv
import numpy as np

img = np.zeros(shape=(500,500), dtype='uint8')

for filas in range(100):
    for columnas in range(100):
        img[filas][columnas] = 255

#for filas in range(400, 500):
#    for columnas in range(400, 500):
#        img[filas][columnas] = 180

for filas in range(100):
    for columnas in range(100):
        img[filas+400][columnas+400] = 180

cv.imshow("Cuadro Negro", img)
k = cv.waitKey(0)

