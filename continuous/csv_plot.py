#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

def main():
    base = np.loadtxt('result_exp.csv', delimiter=',', skiprows=0, usecols=(0,1))[:6]
    x = np.linspace(0.5, 1, 256)
    y = np.exp(x)
    plt.plot(base[:,0], base[:,1])
    plt.plot(x, y)
    plt.show()

    data = np.loadtxt('result_exp.csv', delimiter=',', skiprows=7, usecols=(0,1,2))
    print(data[0][2])


if __name__ == '__main__':
    main()
