# 連続系アルゴリズム

---

# 1. 浮動小数の誤差について

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


### hoge
以下，一貫性不等式を満たすべくtろうと行列のノルムを選び，どのノルムかは明記しない．

$Ax =b$に対して
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