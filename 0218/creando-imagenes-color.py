import cv2 as cv
import numpy as np

img = np.zeros(shape=(500,500,3), dtype='uint8')

for filas in range(100):
    for columnas in range(100):
        img[filas][columnas][0] = 255     # Blue
        img[filas+400][columnas][1] = 255 # Green
        img[filas][columnas+400][2] = 255 # Red
        #Blanco
        img[filas+400][columnas+400][0] = 255
        img[filas+400][columnas+400][1] = 255
        img[filas+400][columnas+400][2] = 255

cv.imshow("Color", img)
k = cv.waitKey(0)

# Guardamos la imagen
cv.imwrite("colores-cuadros.png",img)
