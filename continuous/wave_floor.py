#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import sin, cos, sqrt, pi
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

def generate_f(r, x0):
    def f(x):
        return np.sin(x) + ((x-x0)/np.sqrt(r**2 - (x-x0)**2))
    return f

def bisection(f, a, b):
    s = 0
    for i in range(1000):
        print(a,b)
        if(abs(a-b) < 1e-10):
            break
        s = (a+b)/2.0

        if(f(s)*f(a) < 0):
            b = s
        else:
            a = s
    return s

def falling_time(x, g=9.8):
    t = g*(x**2)/2
    return t

def main():
    # 3Dでの座標情報
    # 球の中心座標
    x0, y0, z0 = 12.0, 0.1, 1
    # 球の半径
    r = 2

    # z軸を通る平面で切った2D(x,y)で考える
    # [-pi:pi]の区間だけを考えれば十分
    #  (x0を区間内に含む、[2k*pi-pi, 2k*pi+pi]の領域にしか落ちないので)
    x0_raw = np.sqrt(x0**2 + y0**2)
    x0 = ((x0_raw + np.pi) % (2*np.pi)) - np.pi
    print(x0_raw, x0)
    y0 = z0

    # fは球と地面の距離の関数の微分
    # y(x) = (y0 - (r^2 - (x-x0)^2)^1/2 ) - cosx の時のdy(x)/dx
    f = generate_f(r, x0)
    # 一応f=0があることの確認
    X = np.linspace(-np.pi, np.pi, 100)
    Y = f(X)
    plt.plot(X, Y)
    plt.show()


    # f=0となるxを求める
    # -pi ~ piの範囲だけを考える
    # 球の直下以外はありえないから、探索は[x0-r:x0+r]の範囲でOK
    # sqrtが0になってしまうので、微小な値を追加している
    x_sol = bisection(f, x0-r+1e-10, x0+r-1e-10)
    print(x_sol)

    # 落ちる時間の計算
    min_distance = y0 - np.sqrt(r**2 - (x_sol - x0)**2) - np.cos(x_sol)
    t = falling_time( min_distance )
    print(t)

main()




