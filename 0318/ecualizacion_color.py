#!/usr/bin/env python3
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Se lee la imagen
#img = cv.imread("../imgs/lenna.jpg")
#img = cv.imread("../imgs/gruta.jpg")
img = cv.imread("../imgs/playa.jpg")

# Obtenemos su forma
fil, col, ch = img.shape

img_YUV   = cv.cvtColor(img, cv.COLOR_BGR2YUV)
img_YCrCb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)

# equalize the histogram of the Y channel
img_YUV[:,:,0] = cv.equalizeHist(img_YUV[:,:,0])
img_YCrCb[:,:,0] = cv.equalizeHist(img_YCrCb[:,:,0])

# convert the YUV image back to RGB format
img_YUV2   = cv.cvtColor(img_YUV, cv.COLOR_YUV2RGB)
img_YCrCb2 = cv.cvtColor(img_YCrCb, cv.COLOR_YCrCb2RGB)

fig, ax = plt.subplots(3,2)
ax[0][0].imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB), vmin=0, vmax=255)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    ax[0][1].plot(histr,color = col)

ax[1][0].imshow(img_YUV2, vmin=0, vmax=255)
ax[1][1].hist(img_YUV[:,:,0].ravel(),256,[0,256])
ax[2][0].imshow(img_YCrCb2, vmin=0, vmax=255)
ax[2][1].hist(img_YCrCb[:,:,0].ravel(),256,[0,256])
plt.show()
