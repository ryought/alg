#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

# dy/dt = f(t,y) の時  y(t) を求める

# t(n+1), y(n+1) = advance(t(n), y(n))
def advance(t, y, f):
    global h
    k1 = f(t,     y)
    k2 = f(t+h/2, y+k1*h/2)
    k3 = f(t+h/2, y+h/2*k2)
    k4 = f(t+h,   y+h*k3)
    y = y + h*(k1 + 2*k2 + 2*k3 + k4)/6
    t = t + h
    return t, y

# t, y = (vx1, vy1, rx1, ry1, vx2, vy2, rx2, ry2)
def f(t, y):
    global G, M, m
    G = 0.1
    M = 1000
    m = 1000
    Y = np.zeros_like(y)
    vx1, vy1, rx1, ry1, vx2, vy2, rx2, ry2 = y

    r = np.sqrt(np.abs(rx1-rx2)**2 + np.abs(ry1-ry2)**2)

    Y = np.array([
            -G*M*m*(rx2-rx1)/r**3,
            -G*M*m*(ry2-ry1)/r**3,
            vx1,
            vy1,
            -G*M*m*(rx1-rx2)/r**3,
            -G*M*m*(ry1-ry2)/r**3,
            vx2,
            vy2                   ])
    return Y

def test_f():
    t = f(10, np.array([1,2,3,4, 5, 6, 7, 8]))
    print(t, type(t))
h = 0.001

def test_runge():
    global h
    N = 100
    t = np.zeros((N, 1))
    y = np.zeros((N, 1))
    t[0] = 0
    y[0] = 0.0001
    for i in range(N-1):
        t[i+1], y[i+1] = advance(t[i], y[i], lambda t,y: -2*y)

    plt.plot(t, y)

    T = np.linspace(0, N*h, 100)
    Y = np.exp(-2*T)*y[0]

    plt.plot(T, Y)
    plt.show()

# test_runge()

def main():
    global h
    N = 10000
    t = np.zeros((N, 8))
    y = np.zeros((N, 8))
    t[0] = 0
    y[0] = [0, 4, 10, 0, 0, -4, -10, 0]
    for i in range(N-1):
        print(i)
        t[i+1], y[i+1] = advance(t[i], y[i], f)
    X1, Y1 = y[:,2], y[:,3]
    X2, Y2 = y[:,6], y[:,7]
    
    plt.scatter(X1, Y1)
    plt.scatter(X2, Y2)
    plt.show()
    

main()

