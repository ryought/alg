# 連続系アルゴリズム 課題6

## 問題1  Fourier変換
$\omega = e^{-2\pi i/K}$の性質を調べる．
- $p(\omega^0)$ 
    $(\omega^0)^i = 1 \in R, \forall i$で，係数$c_i \in R$なので，実数の和と積で表される$p(\omega^0) = \sum_{i=0}^{K-1} c_i (\omega^0)^i$も実数．
- $p(\omega^{K/2})$
    $\omega^{K/2} = -1 \in R$より，上と同様に実数となる．
- $(p(\omega^h))^* = p(\omega^{K-h})$
$\omega^{h} \omega^{K-h} = e^{-2 \pi hi/K} e^{-2 \pi (K-h)i/K} = e^{-2 \pi Ki/K} = 1 \in R$から，2つは複素共役．それに実数を掛けたもの，またそれらの和もまた複素共役の関係にある．つまり$( p(\omega^h))^* = \sum_{i=0}^{K-1} c_i ((\omega^h)^i)^* = \sum_{i=0}^{K-1} c_i (\omega^{K-h})^i = p(\omega^{K-h})$である．

## 問題2  FFTの実装
$K=2^k$点のプログラムを，pythonで再帰を使って実装した．
データ点$\{c_i\}_{i=0}^{K-1}$についての多項式$p(x) = \sum_{i=0}^{K-1} c_i x^i$についてフーリエ変換をすると，$\hat{c}_j = \sum_{s=0}^{K-1} c_s e^{-\frac{2\pi jsi}{K}}$であり，これは$p(x)$に$\omega^j$を代入したもの．なので離散フーリエ変換は計算上は多項式への代入計算と等価である．
再帰で書いた場合は，バタフライ演算になるような順番は考慮せずに作ることができる．

```python
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
```


また，ナイーブな実装として，単純な代入を行うHorner法のプログラムと，それを使ったフーリエ変換とフーリエ逆変換のプログラムは以下．

```python
def horner(c, x):
    v = c[len(c)-1]
    for i in reversed(range(len(c)-1)):
        v = v*x + c[i]
    return v

def dft_naive(c, K):
    w = np.exp(-2*np.pi*1j/K)
    return [ horner(c, w**i) for i in range(K) ]

def idft_naive(c, K):
    w = np.exp(-2*np.pi*1j/K)
    return np.array([ horner(c, w**(-i))/K for i in range(K) ])
```

結果は次のようになり，データ数が大きくなるとFFTの方が実行時間的に有利になった．

\begin{figure}
\centering
\includegraphics[width=0.9\textwidth]{figure/fft2.png}
\caption{FFT($O(K \log K)$)とHorner法($O(K^2)$)の実行時間の比較．ランダムに発生させた$K$個のデータに対して，フーリエ変換の時間を記録した．}
\end{figure}

