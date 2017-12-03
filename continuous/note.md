# 連続系アルゴリズム

---

# 1. 浮動小数の誤差について

# 2. 

# 3. ルンゲクッタ法
## 常微分方程式の初期値問題
常微分方程式の初期値問題 $\frac{dy(x)}{dx} = f(x,y)$を, 初期値$y(0) = y_0$の下で$x=0, X$まで解く．

高階常微分方程式の場合は，連立に帰着できる．$\frac{d^2y(x)}{dx} = f(x,y)$なら，$\frac{dy}{dx} = u, \frac{du}{dx} = f(x,y)$としたらいい．

## 離散変数法
点$0, x_1, ..., x_m=X$を選んで，そこでの関数値$y(x_1), ..., y(x_m)$を近似的に求める．
基本的には$x_1 = h, x_2 = 2h, ..., x_n=nh=X$と等間隔に取る．($h$を刻み幅という)

以下，$y(x_i)$の近似値を$y_i$と書く．
この各点に関して$x_{n+1}$を求める方法が色々ある．


### 前進Euler法
$y_{n+1} = y_n + hf(x_n, y_n)$

#### 局所誤差(各点での厳密解との誤差)
$x_{n+1} = x_n + h$を使って，$y$をTaylor展開すると，$y(x_{n+1}) = y(x_n) + h \frac{dy(x_n)}{dx} + O(h^2) = y(x_n) + h f(x_n, y(x_n)) + O(h^2)$．

厳密値 $y(x_{n+1}) = y(x_n) + h f(x_n, y(x_n)) + O(h^2)$
近似値 $y_{n+1} = y_n + hf(x_n, y_n)$

$y_n = y(x_n)$($n$における近似値が正確)ならば，$| y_{n+1} - y(x_{n+1}) | = O(h^2)$となる．これは**1次の解法**と呼ばれる．


#### 大域誤差(区間の端から端で積もった誤差の合計)
仮定 $|f(x,y) - f(x,z)| \leq L |y-z|$(Lipschitz連続), $|y''(x)| \leq 2M$, $L,M$:正定数

誤差$e_n = y_n - y(x_n)$とおく

$e_{n+1} = y_{n+1} - y(x_{n+1}) = (y_n + hf(x_n, y_n)) - (y(x_n) + hy'(x_n) + \frac{h^2}{2} y''(\xi_n)) = (y_n - y(x_n)) + h(f(x_n, y_n) - f(x_n, y(x_n))) - \frac{h^2}{2} y''(\xi_n)$

$|e_{n+1}| \leq |e_n| + h | f(x_n, y_n) - f(x_n, y(x_n)) | + \frac{h^2}{2} | y''(\xi_n) | \leq |e_n| + hL |e_n| + h^2 M$

$e_0 = 0$とすると，$|e_n| \leq \frac{Mh}{L} ((1+hL)^n -1) \leq h \frac{M}{L} e^{Lnh}$, ($(1+x)^n \leq e^{xn}$より)．

$x_n = X$での誤差は,$|e_n| \leq h \frac{M}{L} e^{LX} = O(h)$ (1次の解法 とした所以)

$h\to 0$で真の解に近づくことがわかる．


### Runge-Kutta法
$y_{n+1} = y_n + h \sum_{i=1}^s b_i k_i, k_i = f(x_n + c_ih, y_n + \sum_{i=1}^s a_{ij} k_j)$

$s$:段数
通常$\sum_i b_i = 1, \sum_j a_{ij} = c_i$

Butcher配列という行列で表せる．$\begin{pmatrix}c & A \\\ & b^\top \end{pmatrix}$

この特殊例として，いくつか種類がある．
### 後退Euler法
$y_{n+1} = y_n + h f(x_{n+1}, y_{n+1})$

$y_{n+1}$についての方程式をとく必要がある．

### 修正Euler法
$k_1 = f(x_n, y_n), k_2 = f(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_1)$として，$y_{n+1} = y_n + h k_2$

$k_1$は開始点$(x_n, y_n)$での傾き,$k_2$は$(x_n + \frac{h}{2}, y_n + \frac{h}{2} k_1)$での傾き，つまり$k_1$の傾きで$(x_n, y_n)$からの線形近似をした時の$x_n+\frac{h}{2}$(区間中間)の点での傾き．

### 改良Euler法
$k_1 = f(x_n, y_n), k_2 = f(x_n + h, y_n + h k_1)$として，$y_{n+1} = y_n + h\frac{k_1 + k_2}{2}$

上の修正Euler法で，$x_n+h$まで進めるバージョン


### RK法
局所誤差が$O(h^{p+1})$の時，$p$次の解法という．1次以上の時「適合的」といい，$h\to 0$で解に収束する.$\sum_i b_i = 1$で成立

「陽的」:$A$が狭義下三角．方程式を解かなくていいということ．それ以外は「陰的」と言われる．

陽的RK法の次数
段 1 2 3 4 6 7 9 11
次数 1 2 3 4 5 6 7 8

陰的RK法の次数: $s$段で$2s$次．


## 線形安定性解析
常微分方程式の初期値問題として，線形関数$f(x,y) = \lambda y, \lambda \in \mathbb{C}$を考える．
解析解は$y = \exp(\lambda x)$.

$y_{n+1} = R(\lambda h) y_n$($R(.)$:多項式)の形にすると，$|R(\bar{h})| > 1$で発散，$|R(\bar{h})| < 1$で収束．

$R(\bar{h}) < 1, \bar{h} = \lambda h$を複素平面上に描く．

定義：絶対安定領域が左半平面を含む時，**A安定** であるという．
定理：陽的RK法はA安定でない．s段2s次陰的RK法でA安定なものがある．


### 例:Euler法
$f(x,y) = \lambda y$とすると，$u_{n+1} = u_n + \lambda h u_n$より，$R(\lambda h) = 1 + \lambda h$．$1 + \bar{h} = r e^{i\theta}$とおいた時に，求める領域は$r < 1$となる$\bar{h}$がいる領域．したがって$\bar{h} = re^{i\theta} - 1, r<1$より，$(-1, 0)$を中心とする半径1の円．

stability.pdfがわかりやすい．


刻み幅制御：誤差を推定しながら，刻み幅を動的に変える．


# 4. 乱数
## 一様乱数
スライド参照

## その他の分布に従う乱数
$p(x)$:確率密度関数 に従う乱数を作る．

### 逆関数法
$f(x) = \int_{-\infty}^x p(t)dt$について，$f^{-1}(x)$が作れる時のみ使える．

1. $(0,1)$の一様乱数$u$を作る($u=0,1$は捨てる)
2. $f^{-1}(u) = x$とした$x$を返す.

### 棄却法
$p(x) \leq \mu q(x)$となる定数$\mu$, 分布$q(x)$を作る．

1. $q(x)$に従う乱数$x$と，$[0,1)$の一様乱数$u$を作る
2. $\mu q(x) u \leq p(x)$ならば採択し，$x$を返す．そうでなければ棄却して1に戻る.

### Box-Muller法
一様乱数から独立な正規分布に従う2乱数を作る方法

中心極限定理を使って,乱数の平均を取ってくるのも簡易的だがあり.

### 別名法 alias method
離散分布の時.

## 乱数の利用:モンテカルロ法
積分の近似値

# 5. 多項式のべき表現
べき表現$p(x) = a_o + a_1x+a_2x^2 + ...$
次数$n$，係数$a_i$,浮動小数

## 問題1: 代入
次数$n$と係数$a_i$が与えられた時,実数$x$に対して$p(x)$を求める．

### ナイーブな実装
$\sum_{k=0}^n a_k x^k$
$x,x^2, ...$と順番に計算する．乗算$a_i x^i$をして，和を求める. 
演算数は乗算$2n-1$, 加算$n$

### Horner method(nested multiplication)
$(((a_4x + a_3)x + a_2)x + a_1)x + a_0$
$a_i$までの和に,$x$をかけて$a_{i-1}$を足す作業を繰り返す感じ

プログラムで書くと下．
```C
v = a[n];
for (k=n-1; k>=0; k--) {
    v = v*x + a[k];
}
return v;
```
演算数は乗算$n$，加算$n$(ループ回数が$n$)．

並列に計算できなくなるが,誤差も少なくなる

## 問題2: 多項式補間,多項式を求める
$n$個の点$\{x_i\}_{i=1}^n$と，それぞれの点での多項式のとる値$v_i = p(x_i)$が与えられている時,$n-1$次多項式$p(x)$を求める．

### 部分問題


## 問題3: 補間,値だけを求める

## 問題4: 多項式補間を多項式の形で求める


# 6.1. FFT
## 離散Fourier変換
### 多項式の変換
関数$f(s)$を$F(r)$に離散フーリエ変換するとは,
$F(r) = \sum_{s=0}^{K-1} f(s) e^{-\frac{2\pi rsi}{K}} = \sum_{s=0}^{K-1} f(s) (\omega^{r})^s$
とすること.
この時逆フーリエ変換があって，
$f(s) = \frac{1}{K} \sum_{r=0}^{K-1} F(r) e^{\frac{2\pi rsi}{K}} = \sum_{r=0}^{K-1} F(r) (\omega^{-s})^r$
となる．
基底$\{ e^{-i\frac{2\pi t}{K}} \}_{t=0}^{K-1}$に関する展開．

ただし$\omega = e^{-\frac{2\pi i}{K}}$.


これは，数列$\{a_n\}_{n=0}^{K-1}$から数列$\{b_n\}_{n=0}^{K-1}$への変換と考えることもできて，
$b_r = \sum_{s=0}^{K-1} a_s e^{-\frac{2\pi rsi}{K}}$
$a_s = \frac{1}{K} \sum_{r=0}^{K-1} b_r e^{\frac{2\pi rsi}{K}}$

さらに，上の数列から多項式$p(x) = \sum_{i=0}^{K-1} a_i x^i, q(t) = \sum_{i=0}^{K-1} b_i t^i$を作った時，上の変換は$p(x)$から$q(t)$への変換とも考えられる．なぜなら上は，$p,q$に$\omega^s, \omega^r$を代入したものだから．
$b_r = \sum_{s=0}^{K-1} a_s (\omega^{r})^s = p(\omega^r)$
同様に
$a_s = \frac{1}{K} q(\omega^s)$

つまり，多項式$p(x)$のフーリエ変換を考えると，変換後の多項式$q(t)$の係数$b_r$は，$p(x)$に$\omega^r$を代入したもの($=p(\omega^r)$)と等しいから，全体では$K$回の代入操作を行うことと等しい．

結局問題は，「べき表現の$K-1$次多項式$p(x)$に対し，全ての$p(\omega^k)$を求めよ．」となる．

### (連続の)Fourier-transformとの関連
なぜこれが離散近似になっているかの説明．
数値計算のツボより．


### 性質
$\omega = e^{-\frac{2\pi i}{K}}, K=2^k$の性質:
- $\omega$は1の$K$乗根, $\omega^K = 1$
- $\omega^{\frac{K}{2}} = -1$
- $\omega^{K+h} = \omega^h$

基底としての性質(直交規定、正規ではない)
- $\sum_{i=0}^{n-1}(\omega^j)^i(\bar{\omega^k})^i = \sum_{i=0}^{n-1}\omega^{i(j-k)} = n(j \equiv k \bmod n), 0(otherwise)$

## 高速Fourier変換 FFT
$p(x)$について$p(\omega^k), k=0,...,K-1$を求める
1. $p(x)$を偶数べきと奇数べきにわける
    $p(x) = q(x^2) + xs(x^2)$, $q(x),s(x)$は$\frac{K}{2} -1$次多項式．
2. $q((\omega^k)^2)$と$s((\omega^k)^2)$を再帰的に計算する
3. くっつける
    $p(\omega^h) = q(\omega^{2h}) + \omega^h s(\omega^{2h})$
    $p(\omega^{\frac{K}{2} + h}) = p(-\omega^h) = q(\omega^{2h}) - \omega^h s(\omega^{2h})$
    
分割統治法．全体で$O(K \log K)$で計算できる.
Horner法で計算すると$O(K^2)$．早い．

## 逆高速Fourier変換 IFFT
$p(\omega^h), h=0,...,K-1$の値が与えられている時，$p(x)$の係数を求める．(多項式補完と同じアイデア)
1. $p(x)$を偶数べきと奇数べきにわける
    $p(x) = q(x^2) + xs(x^2)$, $q(x),s(x)$は$\frac{K}{2} -1$次多項式．
3. 分けた時，
    $p(\omega^h) = q(\omega^{2h}) + \omega^h s(\omega^{2h})$
    $p(\omega^{\frac{K}{2} + h}) = p(-\omega^h) = q(\omega^{2h}) - \omega^h s(\omega^{2h})$
    この左辺が既知なので，連立方程式をといて$q(\omega^{2h}), s(\omega^{2h})$がわかる．再帰的に求めていく．

## 応用例1:多項式の積

多項式$p(x),q(x)$の積$r(x) = p(x)q(x)$を求める

- Kはrの次数より大きなものを選ぶ．
- FFTで$p(\omega^h), q(\omega^h)$を全て求める
    計算量 $O(K\log K)$
- $r(\omega^h) = p(\omega^h)q(\omega^h)$を求める
    計算量 $O(K)$
- IFFTで$r(x)$の係数を求める
    計算量 $O(K\log K)$

## 応用例2:巡回畳み込み
$C_k = \sum_{i=0}^k A_i B_{k-i}$を畳み込みという。

$A\times B = \sum_{i=0}^N \sum_{j=0}^N A_i B_j x^{i+j} = \sum_{k=0}^{2N} A_i B_{k-i} x^k = \sum_{k=0}^{2N} C_k x^k$

$p(x),q(x)$が$K-1$次.

$\hat{r_j} = \sum_{l+m=j} p_l q_m + \sum_{l+m=k+j} p_l q_m = \sum_{l=0}^{K+1} p_l q_{j-q}, (q_j = q_{k-j})$
よくわかんない.

参考
http://stdkmd.com/fftmul/
https://www.slideshare.net/chokudai/fft-49066791
http://www.cfme.chiba-u.jp/~yama/DSP/dsp_04.pdf

# 6.2. 加速
数列の収束を早くするアルゴリズム．

前提：数列$a_n = a + c_1 \lambda_1^n + c_2 \lambda_2^n + ...$($1>|\lambda_1|>|\lambda_2|>...$)

## Richardson加速
$\lambda_1$がわかっていて，$c_1$は未知だとする．
$a_n$と$a_{n-1}$から$\lambda_1$による主要成分を引く．

$a_n' = \frac{a_n - \lambda_1 a_{n-1}}{1-\lambda_1}$
は，収束先の$a$は不変で，より早く収束する．もしも$\lambda_2$も既知なら，より早く収束する．

$a_n = a + c_1 \lambda_1^n + c_2 \lambda_2^n + ...$
$\lambda_1 a_{n-1} = \lambda_1 a + c_1 \lambda_1^n + c_2 \lambda_1 \lambda_2^{n-1} + ...$
より
$a_n - \lambda_1 a_{n-1} = (1-\lambda_1)a + (c_2\lambda_2 - c_2\lambda_1)\lambda_2^{n-1} + ... = (1-\lambda_1)a + (1-\lambda_1) \frac{1-\frac{\lambda_1}{\lambda_2}}{1-\lambda_1} c_2 \lambda_2^n$
より
$a_n' = a + \frac{1-\frac{\lambda_1}{\lambda_2}}{1-\lambda_1}c_2 \lambda_2^n + ...$
ここで$\lambda_2^n$の係数は定数になっている．


## Aitken加速
$\lambda_1,c_1$両方未知だとする．$\lambda_1$を推定することを考える．
$a_n \sim a + c_1 \lambda_1^n$とすると，$\lambda_1 = \frac{a_n - a_{n-1}}{a_{n-1}- a_{n-2}}$

(なぜなら，$b_n = a_n - a_{n-1}$と置くと$b_n = (a+c_1 \lambda_1^n) - (a+c_1 \lambda_1^{n-1}) = c_1(\lambda_1 -1)\lambda_1^{n-1}$であり，$\frac{b_n}{b_{n-1}}=\frac{c_1 (\lambda_1 - 1)\lambda_1^{n-1}}{c_1(\lambda_1 -1)\lambda_1^{n-2}} = \lambda_1$)

これを使って，上のRichardson加速をする．

$a_n' = a_n - \frac{(a_n - a_{n-1})^2}{a_n - 2a_{n-1} + a_{n-2}}$

$a_n' = \frac{a_n - \lambda_1 a_{n-1}}{1-\lambda_1}$

## $\varepsilon$ extroplation
連立方程式で$\lambda_i$を求める感じ

* 数列のタイプで使うべき加速法が違う．なんでも加速できる万能アルゴリズムは存在しないことが示されている．




# 7. 連立一次方程式の解法
## 問題設定 連立一次方程式
$n$次連立方程式を解く．


\begin{eqnarray}
a_{11} x_1 + a_{12} x_2 + ... + a_{1n} x_n = b_1\\
a_{21} x_1 + a_{22} x_2 + ... + a_{2n} x_n = b_2\\
a_{n1} x_1 + a_{n2} x_2 + ... + a_{nn} x_n = b_n
\end{eqnarray}

行列で書くと，$A = \begin{pmatrix}
a_{11} & a_{12} & ...\\\
a_{21} & ...\\\
...
\end{pmatrix}$, $b = \begin{pmatrix} b_1 \\\ b_2 \\\ ... \end{pmatrix}$, $x = \begin{pmatrix} x_1 \\\ x_2 \\\ ... \end{pmatrix}$ とおくと $Ax = b$.

### 前進代入
$A$が下三角行列の場合は，$Ax = b$が簡単に解ける．
$\begin{pmatrix}
a_{11} & 0 & ...\\\
a_{21} & a_{22} & 0 & ...\\\
a_{31} & a_{32} & a_{33} & ...\\\
...
\end{pmatrix} \begin{pmatrix} x_1 \\\ x_2 \\\ x_3 \\\ ... \end{pmatrix} = \begin{pmatrix} b_1 \\\ b_2 \\\ b_3 \\\ ... \end{pmatrix}$

とすると$1$行目は$x_1 = \frac{b_1}{a_{11}}$, $i$行目は$x_i = a_{ii}^{-1} ( b_i - \sum_{j=1}^{i-1} a_ij x_j )$．

### LU分解
下三角と上三角の積に分解する．

$Ax=b$に対して，
1. まず$LU = A$となる下三角行列$L$，上三角行列$U$を求める．($o(n^3)$)
2. $Ly = b$を解く(前進代入)．次に$Ux=y$を解いて$x$を求める．($o(n^2)$) ($o(n^2)$)
	($Ax=b$を$LUx=b$とする．$Ux=y$と置くと，$Ly=b$．

係数が同じなら，2回目以降は$o(n^2)$でできる．

#### 逆行列を求める
$B = A^{-1}$とすると$AB = I$だから，$A b^{(i)} = e^{(i)}$を$n$回計算して$b^{(i)}$を求めることで，$A^{-1}$が求められる．

#### 分解手順
$n\times n$の行列を$(1,n-1) \times (1,n-1)$に分解．

$A = \begin{pmatrix}
a_1 & a_{12}^\top \\\
a_{21} & A_{22} 
\end{pmatrix} = \begin{pmatrix}
l_{11} & 0 \\\
l_{21} & L_{22}
\end{pmatrix} \begin{pmatrix}
u_{11} & u_{12}^\top \\\
0 & U_{22}
\end{pmatrix} = \begin{pmatrix}
l_{11} u_{11} & l_{11} u_{12}^\top \\\
u_{11} l_{21} & l_{21} u_{12}^\top + L_{22}U_{22}
\end{pmatrix}$

$l_{11} = 1$とすると，$u_{11} = a_{11}$, $u_{12}^\top = a_{12}^\top$．この結果を使って$l_{21} = a_{21} / u_{11}$, $L_{22} U_{22} = A_{22} - l_{21} u_{12}^\top$. これを再帰的に計算していく．

- メモリ配置
	分解後の結果を上書きして保存するとメモリ効率がいい．$l_{ii} = 1$なので，保存しておく必要なし．
	$\begin{pmatrix}
	a_{11} & a_{12} & a_{13} & a_{14} \\\
	a_{21} & a_{22} & a_{23} & a_{24} \\\
	a_{31} & a_{32} & a_{33} & a_{34} \\\
	a_{41} & a_{42} & a_{43} & a_{44} \\\
	\end{pmatrix} \mapsto \begin{pmatrix}
	u_{11} & u_{12} & u_{13} & u_{14} \\\
	l_{21} & u_{22} & u_{23} & u_{24} \\\
	l_{31} & l_{32} & u_{33} & u_{34} \\\
	l_{41} & l_{42} & l_{43} & u_{44} \\\
	\end{pmatrix}$
- 枢軸選択
	$u_{11}, a_{11}$が$0$に近いと，$a_{21} / u_{11}$ができない．0でないところと行を交換しておく．(連立方程式は行の交換に関しては不変なので)


### LDU分解
対称行列をLDU分解すると，$L=U^\top$となる．(LDUT分解) LU分解の半分の計算量とメモリ
さらにDが正だと，$LD^{1/2} = L'$とすれば$A=L' L'^\top$．(Cholesky分解)

### QR分解
直交行列と上三角の積に分割する．
(ゼミの内容)

$A = QR$, $Q$:直交行列($Q Q^\top = I$, 基底ベクトルが正規直交), $R$:上三角行列


## 問題設定 固有値
行列$A$の絶対値最大の固有値とそれに対応する固有ベクトルを求めよ．
### ベキ乗法
行列$A$の絶対値最大の固有値$\lambda$が単純な時(重解がない時),適当な初期ベクトル$x_0$から，$y_k = A x_{k-1}, x_k = \frac{y_k}{|| y_k ||}$(正規化)を繰り返すと，$x_k \to x(\lambda)$(固有ベクトル)．

証明
$A$が$n$個の一次独立な固有ベクトル$u_i$を持つと仮定すると，初期ベクトル$x_0$は$x_0 = \sum_{i=1}^n c_i u_i$と表せる．
$A^k x_0 = A^k \sum_{i=1}^n c_i u_i = \sum_{i=1}^n c_i \lambda_i^k u_i$, $A u_i = \lambda_i u_i$,$A^k u_i = A^{k-1} \lambda_i u_i = ... = \lambda_i^k u_i$で，固有値$\lambda_i$と固有ベクトル$u_i$が対応．ソートされているとすると，$A^k x_0 = \lambda_1^k ( c_1 u_1 + \sum_{i=2}^n c_i (\frac{\lambda_i}{\lambda_1})^k u_i \to \tau u_1$

これで固有ベクトル$u_1$を求めたら，$\lambda_1 = \frac{u_1 A u_1}{||u_1||^2}$ (なぜなら$Ax = \lambda x, x^\top A x = x^\top \lambda x, \lambda = \frac{x^\top A x}{x^\top x}$) とすると固有値がもとまる．


### 逆反復法, Raylergh商反復法
最大固有値ではなく，$\sigma$に最も近い固有値を求める．

$(A-\sigma I)^{-1}$の固有値が$\frac{1}{\lambda - \sigma}$になる．($\sigma$に一番近い固有値が最大になる)
$(A-\sigma I)^{-1}$に上のべき乗法を使うと，$\sigma$に一番近い固有値が求められる．

各ステップで，$\sigma =$得られた近似固有値とすると，より早く収束する．
$y_k = (A- \sigma_{k-1} I)^{-1} x_{k-1}, x_k = \frac{y_k}{||y_k||}, \sigma_k = \frac{y_k^\top A y_k}{y_k^\top y_k}$

# 8. 
$Ax = b$の真の解$x$，近似解$\tilde{x}$
- 誤差 $e = \tilde{x} - x$
- 残差 $r = A \tilde{x} - b$
誤差の最小化と，残差の最小化は意味が違う

## ベクトル空間のノルム公理
### ノルム
- $||u|| \geq 0$
- $||\alpha u || = |\alpha| ||u||$
- $||u+v|| \leq ||u|| + ||v||$ (三角不等式)

### 距離
- $d(u,v)\geq 0$, $d(v,u)=0 \leftrightarrow v=u$
- $d(u,v) = d(v,u)$
- $d(u,v) \leq d(u,w) + d(w,v)$

ノルム$|| . ||$に対して， $d(u,v) = ||u-v||$は距離

### ベクトルのノルムの各種
#### 2ノルム Euclidノルム
$||x||_2 = \sqrt{\sum_{i=1}^n |x_i|^2}$
#### 1ノルム
$||x||_1 = \sum_{i=1}^n |x_i|$

#### $\infty$ノルム 最大値ノルム
$||x||_\infty = \max_i |x_i|$

注：定数倍の違いしかない．
$||u||_\infty \leq ||u||_2 \leq ||u||_1$
$||u||_1 \leq \sqrt{2} ||u||_2 \leq 2 || u||_\infty$
(n=2の場合)

図：n=2の時の，$||x||_1 = 1, ||x||_2=1, ||x||_\infty=1$を図示したもの

### 行列のノルムの各種
#### Frobeniusノルム
$||A||_F = \sqrt{\sum_{i=1}^n \sum_{j=1}^n |a_{ij}|^2}$

これは一貫性(consistency)を満たす．(ベクトルをかけてベクトルになった時の2ノルムと対応)
$||Ax||_2 \leq ||A||_F ||x||_2$
$||AB||_F \leq ||A||_F ||B||_F$

注: $||I||_F = \sqrt{n}$


#### 作用素ノルム
ベクトルのノルム$||.||_p$を選ぶ
$||A||_p = \sup_{x\neq 0} \frac{||Ax||_p}{||x||_p} = \sup_{||x||=1} ||Ax||_p$

その行列がベクトルを何倍にするか

- 一貫性をもつ
    $||Ax||_p \leq ||A||_p ||x||_p$
    $||AB||_p \leq ||A||_p ||B||_p$
- $||I||_p = 1$
- 直行行列$Q$に対して，$||Q||_2 = 1$

#### 1ノルム(列和ノルム)
列の和の最大値
$||A||_1 = \max_j \sum_{i=1}^n |a_{ij}|$

#### 無限大ノルム(行和ノルム)
行の和の最大値
n行一列のベクトル(縦ベクトル)の時に，ベクトルの無限大ノルムと一致
$||A||_\infty = \max_i \sum_{j=1}^n |a_{ij}|$

#### 2ノルム(スペクトルノルム)
$||A||_2 = \sqrt{\max_{\lambda \in \lambda(B)} \lambda A^\top A}$
$\lambda(B)$は$B$の固有値の集合


### 連立方程式の誤差の解析
以下，一貫性不等式を満たすベクトルと行列のノルムを選ぶ．
その条件のもとでどのノルムを選ぶかは関係ない．

$Ax=b$に対して
#### 係数の誤差
係数に誤差が入った方程式$\tilde{A}\tilde{x} = b$

誤差
$\tilde{x}-x = \tilde{A}^{-1}b - A^{-1}b = (\tilde{A}^{-1}-A^{-1})b = A^{-1}(A-\tilde{A})\tilde{A}^{-1}b$

その相対誤差っぽいもの
$\frac{||\tilde{x} - x||}{||\tilde{x}||} = \frac{A^{-1}(A-\tilde{A})\tilde{A}^{-1}b}{||\tilde{x}||} \leq \frac{||A^{-1}|| ||A-\tilde{A}|| ||\tilde{A}^{-1} b||}{||\tilde{x}||} = ||A||||A^{-1}|| \frac{||A-\tilde{A}||}{||A||}$

条件数$\kappa(A) = ||A|| ||A^{-1}|| \geq ||I|| \geq 1$
$A$の相対誤差$\frac{||A-\tilde{A}||}{||A||}$と置くと

$\frac{||\tilde{x}-x||}{\tilde{x}} \leq \kappa (A) \frac{||\tilde{A}-A||}{||A||}$

⭐️ 相対誤差は，係数行列の相対誤差の条件数倍で抑えられる
$\kappa(A)\geq 10^{16}$は倍精度では解けない．



#### 右辺の誤差
右辺が少しずれた方程式$A\tilde{x} = \tilde{b}$

$\frac{||\tilde{x}-x||}{||x||} = \frac{||A^{-1}\tilde{b} - A^{-1}b||}{||x||} = \frac{||A^{-1}(\tilde{b} - b)||}{||x||} \leq \frac{||A^{-1}|| ||\tilde{b}-b||}{||x||} = \frac{||A^{-1}|| ||b||}{||x||} \frac{||\tilde{b}-b||}{||b||}$

$\eta = \frac{||A^{-1}|| ||b||}{||x||}$と置くと
$||x|| = ||A^{-1}b|| \leq ||A^{-1}||||b||$ より $1\leq \eta \leq \kappa(A)$

$||A^{-1}|| ||b|| = ||A^{-1}|| ||Ax|| \leq ||A^{-1}|| ||A|| ||x||$

$\frac{||A^{-1}|| ||b||}{||x||} \leq \frac{||A^{-1}|| ||A|| ||x||}{||x||} = \kappa(A)$

### 相対誤差と相対残差
$e = \tilde{x} - x$, $r = A\tilde{x} -b$, ($r=Ae$)
相対誤差$\frac{||e||}{||x||}$, 相対残差$\frac{||r||}{||b||}$

$\frac{||e||}{||x||} = \frac{||A^{-1}r||}{||x||} \leq  \frac{||A^{-1}|| ||r||}{||x||} = \frac{||A^{-1}|| ||b||}{||x||} \frac{||r||}{||b||}$
条件数が大きいと，解がきちんと求まらない


### 反復改良
LU分解にも丸め誤差が入る．$A \simeq LU = \tilde{A}$
それを使って前進後退代入で求めているものは$\tilde{x} = \tilde{A^{-1}} b$(係数に誤差が入ったバージョン)

$x = \tilde{x} - A^{-1} (A \tilde{x} - b)$の$A^{-1}$を$\tilde{A}^{-1}$に置き換える．

反復改良
以下を1,2回繰り返す
$x^{(k+1)} = x^{(k)} - \tilde{A}^{-1}(A x^{(k)} - b)$


どのくらい精度が上がるか
$A x^{(k)} - b = A (x^{(k)} - x)$
$x^{(k+1)} - x = x^{(k)} - x - \tilde{A}^{-1} (A x^{(k)} - b) = (I-\tilde{A}^{-1} A) (x^{(k)} - x) = (I- \tilde{A}^{-1} A)^k (x^{(1)} - x)$

$I-\tilde{A}^{-1} A$の固有値の絶対値が最大のものが1未満なら収束．

- $\tilde{A}^{-1}$にLU分解を使えば，1,2回で十分
- $\tilde{A}^{-1}$は相当荒い近似でも可
- 収束後は残渣は丸め誤差くらいまで減る