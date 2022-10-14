#!/usr/bin/python3

from vectors import Vector_2D
import numpy as np
import matplotlib.pyplot as plt

a = 0
space = np.full((31, 31), 0, dtype='uint8')
k = (15,15)
l = 10
A = Vector_2D(k, l, a)
B = Vector_2D(A.end_point, l, a + 90)
C = Vector_2D(B.end_point, l, a + 180)
D = Vector_2D(C.end_point, l, a + 270)

for idx in A.get_points():
    space[idx] = 255

for idx in B.get_points():
    space[idx] = 255

for idx in C.get_points():
    space[idx] = 255

for idx in D.get_points():
    space[idx] = 255

plt.imshow(space.T, cmap='gray')
plt.show()