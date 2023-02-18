import cv2 as cv
import sys

img_color = cv.imread("../imgs/lenna.jpg")
img_grises = cv.imread("../imgs/lenna.jpg", cv.IMREAD_GRAYSCALE)

# Tipo de dato
print("type color:", type(img_color) )
print("type grises:", type(img_grises) )

# Tamaño de las dimensiones de la matriz
print("shape color:",  img_color.shape )
print("shape grises:", img_grises.shape )

# Dimensiones de la matriz
print("ndim color:",  img_color.ndim )
print("ndim grises:", img_grises.ndim )

