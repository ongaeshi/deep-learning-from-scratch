import numpy as np
import matplotlib
matplotlib.use('tkagg')
import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('lena.png')
plt.imshow(img)

plt.show()
