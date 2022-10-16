#!/usr/bin/python3

from vectors import Vector_2D
import numpy as np
import matplotlib.pyplot as plt

k = (15,15)
l = 10
A = Vector_2D(k, l, 0)
B = Vector_2D(A.end_point, l, 90)
C = Vector_2D(B.end_point, l, 180)
D = Vector_2D(C.end_point, l, 270)


a = 15
A.angle = a + 0
B.angle = a + 90
C.angle = a + 180
D.angle = a + 270
B.start_point = A.end_point
C.start_point = B.end_point
D.start_point = C.end_point

space = np.full((31, 31), 0, dtype='uint8')

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