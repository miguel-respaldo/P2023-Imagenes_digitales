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

# Tipo de dato
print("dtype color:",  img_color.dtype )
print("dtype grises:", img_grises.dtype )

# u -> unsigned -> sin signo
# int -> integer -> entero
# 8 -> 8 bits -> 1 byte -> 0..255
