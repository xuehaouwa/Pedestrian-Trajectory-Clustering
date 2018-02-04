"""
2018.02.03

@author: Hao Xue
"""

# from math import *
import math

PIXELS_IN_METER = 3.33


def euclidDist(p1, p2):
    assert (len(p1) == len(p2))
    return math.sqrt(sum([((p1[i] - p2[i]) / PIXELS_IN_METER) ** 2 for i in range(len(p1))]))
