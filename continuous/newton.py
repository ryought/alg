#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    a = 5
    x = 0.21
    N = 100
    # f(x) = 1/x - a  について  f(x)=0を求める
    for i in range(N):
        x = 2*x - a*(x**2)
    print('final', x)

main()


