#!/usr/bin/python3

from math import pi, cos, sin
import numpy as np
import matplotlib.pyplot as plt

space = np.full((310, 310), 0, dtype='uint8')

for t in range(360):
    a = 100
    b = 50
    size = 150

    t  = (t * pi) / 180
    x = int(round(a * sin(t), 0)) + size
    y = int(round(b * cos(t), 0)) + size

    space[x, y] = 255

plt.title("a = 100; b = 50\nt = range(360)")
plt.imshow(space.T, cmap='gray')
plt.show()