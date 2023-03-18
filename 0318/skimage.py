#!/usr/bin/env python3
#from skimage import exposure
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
#import skimage

imagen = skimage.io.imread("../img/playa.jpg")

# Estiramiento de contraste
p2, p98 = np.percentile(imagen, (2,98))
img_rescale = skimage.exposure.rescale_intensity(imagen, in_range=(p2,p98))

# Ecualización
img_eq = skimage.exposure.equalize_hist(imagen)

# Ecualización adaptiva
img_adapteq = skimage.exposure.equalize_adapthist(imagen, clip_limit=0.03)


fig, ax = plt.subplots(2,2)

ax[0][0].imshow(img_eq)
ax[0][1].hist(img_eq.ravel())
ax[1][0].imshow(img_adapteq)
ax[1][1].hist(img_adapteq.ravel())
plt.show()
