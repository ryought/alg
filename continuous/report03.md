# 連続系アルゴリズム 第3回宿題

## 前進Euler法の絶対安定領域を求める
前進Euler法は$y_{n+1} = y_{n} + f(x_n, y_n) h$である。
これを使って、$\frac{dy}{dx} = f(x, y) = \lambda y, \lambda \in C$を解くことを考える。
$$y_{n+1} = y_n + \lambda y_n h = (1+\lambda h) y_n$$
となる。$y_{n+1} = R(\hat{h}) y_n, \hat{h} = \lambda h$と置くと、安定関数$R(\hat{h}) = 1+\hat{h}$である。絶対安定領域は$\{ \hat{h}: |R(\hat{h})| < 1 \}$なので、複素平面上に図示すると次のようになる。

\begin{figure}
\centering
\includegraphics[width=0.4\textwidth]{figure/region.png}
\end{figure}



## 2体間の万有引力のシミュレーション
4次のルンゲクッタ法で計算した。以下物体1(質量M)、物体2(質量m)とする。

### スイングバイ
$M=10000, m=10$として、原点にある物体1に向けて物体2を、初速度$v_0 = (10, 10)$初期位置$r_0 = (-10, -20)$で発射して、衛生と惑星のスイングバイのような現象をシミュレーションした。
\begin{figure}
\centering
\includegraphics[width=0.4\textwidth]{figure/swingby.png}
\end{figure}


### 円運動させた時の解析解との比較
$M=m=100$で、定常的に円運動している時の半径・速度を初期状態として、シミュレーションによってその先を計算した。そしてその時の半径$r=\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$の時間変化を追った。解析解であれば、$r$は最初と同じ値を取り続けるはずだが、そこからのブレとその絶対値を観察した。
グラフからわかるように、誤差の絶対値は$h$の変化に伴い半分になっていることがわかる。

\begin{figure}
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/largeH.png}
\caption{$h=10^{-2}$の時}
\end{minipage}
\hfill
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/smallH.png}
\caption{$h=10^{-2}/2$ の時}
\end{minipage}
\end{figure}

以下はプログラムのソースコード
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

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
def generate_f(M, m, G):
    def f(t, y):
        Y = np.zeros_like(y)
        vx1, vy1, rx1, ry1, vx2, vy2, rx2, ry2 = y

        r = np.sqrt(np.abs(rx1-rx2)**2 + np.abs(ry1-ry2)**2)
        # モデルの運動方程式は
        # M\frac{d^2 r1}{dt^2} = GMm(r')/|r'|^3
        # m\frac{d^2 r2}{dt^2} = GMm(r')/|r'|^3
        Y = np.array([
                G*m*(rx2-rx1)/r**3,
                G*m*(ry2-ry1)/r**3,
                vx1,
                vy1,
                G*M*(rx1-rx2)/r**3,
                G*M*(ry1-ry2)/r**3,
                vx2,
                vy2                   ])
        return Y
    return f

# fの出力テスト
def test_f():
    t = f(10, np.array([1,2,3,4, 5, 6, 7, 8]))
    print(t, type(t))


# 単振動のモデル
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



def simulation(M, m, G, N, y0):
    global h
    t = np.zeros((N, 8))
    y = np.zeros((N, 8))
    t[0] = 0
    y[0] = y0
    f = generate_f(M, m, G)

    for i in tqdm(range(N-1)):
        t[i+1], y[i+1] = advance(t[i], y[i], f)

    X1, Y1 = y[:,2], y[:,3]
    X2, Y2 = y[:,6], y[:,7]
    plt.scatter(X1, Y1)
    plt.scatter(X2, Y2)
    plt.show()
    return t, y

# スイングバイ
h = 1.0e-2
simulation(M=10000, m=10, G=0.1, N=200, y0=np.array([0, 0, 0, 0, 10, 10, -10, -20]))

# 円運動
M, m = 100, 100
G = 0.1
r0 = 10
a0 = G*m/(2*r0)**2
v0 = np.sqrt(a0 * r0)
# _ = simulation(M=M, m=m, G=G, N=10000, y0=np.array([0, v0, r0, 0, 0, -v0, -r0, 0]))

h = 1.0e-2
t, y = simulation(M=M, m=m, G=G, N=100000, y0=np.array([0, v0, r0, 0, 0, -v0, -r0, 0]))
plt.plot(t, ((y[:,2] - y[:,6])**2 + (y[:,3] - y[:,7])**2))
plt.show()

h = 0.5e-2
t, y = simulation(M=M, m=m, G=G, N=200000, y0=np.array([0, v0, r0, 0, 0, -v0, -r0, 0]))
plt.plot(t, ((y[:,2] - y[:,6])**2 + (y[:,3] - y[:,7])**2))
plt.show()
```

