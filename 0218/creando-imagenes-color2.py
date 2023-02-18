import cv2 as cv
import numpy as np

img = np.zeros(shape=(400,256,3), dtype='uint8')

for filas in range(100):
    for columnas in range(256):
        img[filas][columnas][0] = columnas
        img[filas+100][columnas][1] = columnas
        img[filas+200][columnas][2] = columnas
        #Blanco
        img[filas+300][columnas][0] = columnas
        img[filas+300][columnas][1] = columnas
        img[filas+300][columnas][2] = columnas

cv.imshow("Color", img)
k = cv.waitKey(0)

# Guardamos la imagen
cv.imwrite("colores-cuadros-varios.png",img)
