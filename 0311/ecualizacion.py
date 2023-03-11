#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Se lee la imagen
img = cv.imread("../imgs/gruta.jpg")

# Obtenemos su forma
fil, col, ch = img.shape

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
img_equa = cv.equalizeHist(img_gray)

fig, ax = plt.subplots(2,2)
ax[0][0].imshow(img_gray, cmap='gray', vmin=0, vmax=255)
ax[0][1].hist(img_gray.ravel(),256,[0,256])
ax[1][0].imshow(img_equa, cmap='gray', vmin=0, vmax=255)
ax[1][1].hist(img_equa.ravel(),256,[0,256])
plt.show()
