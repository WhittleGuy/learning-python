#!/bin/python

import numpy as np


def generatePoint():
    x = np.random.uniform()
    y = np.random.uniform()
    return x, y


def getDist(x, y):
    return np.power(np.power(x, 2) + np.power(y, 2), 0.5)


def main():
    RADIUS = 1
    points = int(input('Number of points: '))
    contained = 0

    for n in range(points):
        x, y = generatePoint()
        dist = getDist(x, y)
        if dist <= RADIUS:
            contained += 1
        else:
            pass

    print(4*(contained/points))


if __name__ == '__main__':
    main()
