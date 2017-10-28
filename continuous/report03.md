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


\footnote{ \url{ http://equal-l2-works.hatenablog.com/entry/2015/09/22/094013 } }
\footnote{ \url{http://kurodalab.bs.s.u-tokyo.ac.jp/ja/member/Yugi/Textbook/chapter3.pdf }}

## 2体間の万有引力のシミュレーション
RK4でといた

物体1(質量M)、物体2(質量m)とする。

### スイングバイ
$M=10000, m=10$として、原点にある物体1に向けて物体2を、初速度$v_0 = (10, 10)$初期位置$r_0 = (-10, -20)$で発射して、衛生と惑星のスイングバイのような現象をシミュレーションした。
\begin{figure}
\centering
\includegraphics[width=0.4\textwidth]{figure/swingby.png}
\end{figure}


### 円運動させた時の解析解との比較
$M=m=100$で、定常的に円運動している時の半径・速度を初期状態として、シミュレーションによってその先を計算した。そしてその時の半径$r=\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$の時間変化を追った。解析解であれば、$r$は最初と同じ値を取り続けるはずだが、そこからのブレとその絶対値を観察した。

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


