# 連続系アルゴリズム 1

## $y = \cos x$の誤差解析

浮動小数に変換した時の誤差を$fl(x) = x + \epsilon |x|$として考える。
見積もるべき絶対誤差は、計算結果を$\hat{y} = fl( \cos(fl(x)))$、理論値を$y=\cos x$とした時の、(1)絶対誤差$\hat{y} - y$と(2)相対誤差$\frac{\hat{y}-y}{y}$である。

一次近似をして$\cos(x+\delta x) = \cos x - \sin x \delta x$より、$\hat{y} = fl(\cos (fl(x))) = fl(\cos x - \sin x \epsilon |x|) = \cos x - \sin x \epsilon |x| + \epsilon | \cos x - \sin x \epsilon |x| |$

絶対誤差は
\begin{align}
-\sin(x) \epsilon |x| + \epsilon | \cos (x) - \sin (x) \epsilon |x| |
\end{align}
となる。

## $|x| \to \infty$ の場合
(1)式の$|x| \to \infty$極限をとると、絶対誤差が無限大になることからわかる。


## $|x| \to 0$の場合の$1-\cos x$の相対誤差
値の近い2数の引き算では相対誤差が大きくなりやすい


## 衝突時間の計算
`collision_time.c`に実装しました。
