import cv2 as cv
import numpy as np

img = np.zeros(shape=(500,500,3), dtype='uint8')

for filas in range(100):
    for columnas in range(100):
        img[filas][columnas][0] = 255
        img[filas][columnas+100][1] = 255
        img[filas][columnas+200][2] = 255

cv.imshow("Color", img)
k = cv.waitKey(0)
