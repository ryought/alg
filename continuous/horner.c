#include <stdio.h>
#include <math.h>

/*
 * n!を計算
 */
double frac(int n) {
  double r = 1;
  for(int i=1; i<=n; i++){
    r = r*(double)i;
  }
  return r;
}

/*
 * nevilleのアルゴリズムで，0.5~1.0まで0.1刻みのデータ点を元に，0.75を推定
 */
double neville(double* v) {
  // 補間 
  // Nevilleのアルゴリズムを使う
  // x = 0.75の値を求める
  double P[6][6];
  double xj, xk;
  double X = 0.75;
  // 初期化 各点の座標を入れておく
  for(int i=0; i<6; i++) {
    P[i][0] = v[i]; //f(x_i)を入れる
  }
  // 補間
  for(int j=1; j<6; j++){
    // 長さ(j+1)について
    for(int k=0; k<6-j; k++){
      xj = 0.5 + 0.1*k;
      xk = 0.5 + 0.1*(k+j);
      P[k][j] = ( (X-xk)*P[k][j-1] - (X-xj)*P[k+1][j-1] ) / (xj - xk); 
    }
  }
  return P[0][5];
}

/*
 * horner法で，\sum_{k=0}^{n-1} an[k] x^k の値を代入計算
 *  an: an[i]はx^iの係数
 *  n: anの要素数．xの最高次数-1でもある
 */
double horner(int n, double* an, double x) {
  double y = an[n-1];
  for(int i=n-2; i>=0; i--) {
    y = y*x + an[i];
  }
  return y;
}

void horner_and_neville(int n, double* an) {
  // x = 0.5 - 1.0の値を格納
  double v[6];
  double x;

  for(int I=0; I<6; I++) {
    x = 0.5 + 0.1*I;
    v[I] = horner(n, an, x);
  }

  // neville
  double interpolated = neville(v);
  printf("interpolated: %lf\n", interpolated);

  // 誤差の判定
  double exact;
  // horner法
  exact = horner(n, an, 0.75); 
  printf("exact: %lf\n", exact);

  // ずれ
  // double型小数を表示する
  // 全体桁数25,小数点以下桁数20
  printf("error: %25.20lf\n", interpolated - exact);

}


int main(void) {
  // 多項式
  double A[10];
  for(int i=0; i<10; i++) {
    A[i] = 1;
  }
  for(int j=3; j<=8; j++){
    printf("1+x %d\n", j);
    horner_and_neville(j, A);
  }

  // 指数
  double E[10];
  for(int i=0; i<10; i++) {
    E[i] = 1/frac(i);
    printf("%lf\n", E[i]);
  }
  horner_and_neville(10, E);

  // 対数
  double L[6];
  for(int i=0; i<6; i++) {
    L[i] = log(0.5 + 0.1*i);
    printf("%lf\n", L[i]);
  }
  printf("%lf\n", neville(L));
  printf("ex: %lf\n", log(0.75));

  return 0;
}
