#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from lib import runningtime

# 点数
# \omega

# 参考
# https://qiita.com/unsolvedprobrem/items/ba1cd3c668071059ab18


def horner(c, x):
    """
    @param c = [c[i]] n-1次多項式
    @param x 代入する値
    @return \sum c[i] x^i
    """
    v = c[len(c)-1]
    for i in reversed(range(len(c)-1)):
        v = v*x + c[i]
    return v


def dft_naive(c, K):
    """
    c: coefficients [c0, ..., c(k-1)]
    return: [f(w*k)]_k=0^k=K-1
    """
    w = np.exp(-2*np.pi*1j/K)
    return [ horner(c, w**i) for i in range(K) ]

def idft_naive(c, K):
    """
    フーリエ逆変換 ナイーブ実装
    cはフーリエ級数
    """
    w = np.exp(-2*np.pi*1j/K)
    return np.array([ horner(c, w**(-i))/K for i in range(K) ])

# @timeit
def fft(p, K):
    """
    \sum_{i=0}^K-1 c[i]x^i の フーリエ変換を返す プログラム
    """
    if len(p) == 1:
        # 再帰の終了条件
        return p
    # 再帰する
    # 分割
    q = p[::2]  # 偶数べき
    s = p[1::2]   # 奇数べき
    # 再帰計算
    Q, S = fft(q, K//2), fft(s, K//2)
    w = np.exp(-2*np.pi*1j/K)
    R = [0 for _ in range(K)]
    for i in range(len(p)//2):
        R[i      ] = Q[i] + w**i * S[i]
        R[i +K//2] = Q[i] - w**i * S[i]
    return R

def test_fft():
    # 音波作成
    # https://jp.mathworks.com/help/matlab/ref/fft.html
    pass

def experiment_env(i):
    K = 2**i
    np.set_printoptions(precision=3, suppress=True)
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
    # print(horner([1,1,1,1,1], 1))
    r = np.random.random_sample(K)
    # r = np.ones(K) * 2
    # print(r)
    # print('fft',   np.array(fft(r, K)))
    # print('naive', np.array(dft_naive(r, K)))
    # print('fft',   idft_naive(np.array(fft(r, K)), K))
    # print('naive',   idft_naive(dft_naive(r, K), K))

    import timeit
    t1 = timeit.timeit(lambda: dft_naive(r, K), number=10)/10
    t2 = timeit.timeit(lambda: fft(r, K), number=10)/10
    return [t1, t2]


if __name__ == '__main__':
    result = []
    for i in range(2,12):
        t = experiment_env(i)
        result.append(t)
        print('{0}\t{1}\t{2}'.format(i, t[0], t[1]))
    result = np.array(result)
    plt.plot(np.arange(2,12), result[:,0], label='naive dft')
    plt.plot(np.arange(2,12), result[:,1], label='fft')
    plt.yscale('log')
    plt.ylabel('time (ms)')
    plt.xlabel('n (K=2^n)')
    plt.legend()
    plt.show()
    print(result[:,0])

