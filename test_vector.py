#!/usr/bin/python3

from vectors import Vector_2D
import time

t_start = time.time()
v = Vector_2D((2,2), 3, 1000000000000)
print(time.time() - t_start)