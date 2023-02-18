import cv2 as cv
import sys

img_color = cv.imread("../imgs/lenna.jpg")
img_grises = cv.imread("../imgs/lenna.jpg", cv.IMREAD_GRAYSCALE)

# cv.IMREAD_GRAYSCALE en escala de grises
# cv.IMREAD_COLOR en color (default) formato de 8-bits BGR
# cv.IMREAD_UNCHANGED lee con todo y alphas

if img_color is None:
    sys.exit("La imagen no existe")

cv.imshow("Lenna Gris", img_grises)
cv.imshow("Lenna Color", img_color)


k = cv.waitKey(0)
