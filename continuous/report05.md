# 連続系アルゴリズム 課題5

## 問題1
$I = [1,2]$での$\frac{1}{x}$の一次多項式近似をする．


誤差関数$E(x) = \frac{1}{x} - p(x)$, $p(x) = ax + b$とする．

条件は
- 極値(端点を含む)は$x=1,2,t$($1<t<2$)の3点でとる．
    $E'(t) = 0$
- その三か所の極値の絶対値は等しく，符号は交互になる．
    $E(1) = - E(t) = E(2)$
未知数は$t,a,b$の3つで，3つ等式ができたので，連立方程式をとく．

$E(x) = \frac{1}{x} - ax - b$, $E'(x) = \frac{-1}{x^2} -a$である．また$E(1) = 1-a-b, E(2) = \frac{1}{2} - 2a -b$だから，

\begin{align}
\begin{cases}
    \frac{-a(t^2 + \frac{1}{a})}{t^2} = 0 \\
    1-a-b = \frac{1}{2} -2a -b \\
    1-a-b = - \frac{1}{t} + at+b \\
\end{cases}
\end{align}

(2)式から,$a=-\frac{1}{2}$．(1)式に代入して，$t^2 - 2 =0$より$t=\sqrt{2}$．最後に(3)に代入して，$b = \frac{3}{4} + \frac{\sqrt{2}}{2}$．

検証のために，これをプロットした．

\begin{figure}
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/error_function.png}
\caption{求めた$t,a,b$の時の$E(x)$のグラフ．上の条件が満たされていることがわかる．また誤差が最大で0.04程度あることもわかる．}
\end{minipage}
\hfill
\begin{minipage}{0.45\hsize}
\centering
\includegraphics[width=0.9\textwidth]{figure/zentai.png}
\caption{$p(x)$と$\frac{1}{x}$を描画したもの．}
\end{minipage}
\end{figure}

## 問題2
Horner法で多項式の値を計算し，その値を元にNevilleのアルゴリズムで多項式補間する．

多項式$1+x+x^2+x^3+...$

$\exp(x)$
```
interpolated: 0.750000,    2.11700001024082684609
exact: 0.750000,    2.11699999996594012686
error:    0.00000001027488671923
```

$\log(x)$
