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
    Y = np.zeros_like(y)
    vx1, vy1, rx1, ry1, vx2, vy2, rx2, ry2 = y

    r = np.sqrt(np.abs(rx1-rx2)**2 + np.abs(ry1-ry2)**2)

    Y = np.array([
            G*M*m*(rx2-rx1)/r**3,
            G*M*m*(ry2-ry1)/r**3,
            vx1,
            vy1,
            G*M*m*(rx1-rx2)/r**3,
            G*M*m*(ry1-ry2)/r**3,
            vx2,
            vy2                   ])
    return Y

def test_f():
    t = f(10, np.array([1,2,3,4, 5, 6, 7, 8]))
    print(t, type(t))

h = 1.0e-3
G = 0.1
M = 100000
m = 10
r0 = 10
a0 = G*m/(2*r0)**2
v0 = 2.0
N = 20000
print(a0, v0, r0)


def main2():
    global h, G, M, m, r0, v0, N
    t = np.zeros((N, 2))
    y = np.zeros((N, 2))
    t[0] = 0
    y[0] = [10, 0]
    for i in range(N-1):
        t[i+1], y[i+1] = advance(t[i], y[i], lambda t, y: np.array([y[1], -y[0]]))
    plt.plot(t, y[:,0])
    plt.show()

def main():
    global h, G, M, m, r0, v0, N
    t = np.zeros((N, 8))
    y = np.zeros((N, 8))
    t[0] = 0
    y[0] = [0, v0, r0, 0, 0, -v0, -r0, 0]
    for i in range(N-1):
        t[i+1], y[i+1] = advance(t[i], y[i], f)
    X1, Y1 = y[:,2], y[:,3]
    X2, Y2 = y[:,6], y[:,7]
    
    plt.scatter(X1, Y1)
    plt.scatter(X2, Y2)
    plt.show()
    

# main()
main2()


