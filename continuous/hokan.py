#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
1/x, I=[1,2] を p(x)=ax+b で近似する例．
レポート課題5に対応
"""

import numpy as np
import matplotlib.pyplot as plt

def test_1():
    x = np.linspace(1, 2, 256)
    a, b = - 1/2, 3/4 + np.sqrt(2)/2
    E = 1/x - a*x - b

    plt.plot(x, E)
    plt.show()

    x = np.linspace(0.5, 2.5, 256)
    A = 1/x
    B = a*x + b
    plt.plot(x,A, label='1/x')
    plt.plot(x,B, label='ax+b, a=-1/2, b=3/4 + 1/sqrt(2)')
    plt.legend()
    plt.show()



if __name__ == '__main__':
    test_1()
