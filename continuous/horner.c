#include <stdio.h>

double frac(int n) {
  double r = 1;
  for(int i=1; i<=n; i++){
    r = r*(double)i;
  }
  return r;
}


void horner_and_neville(int n, double* an) {
  // x = 0.5 - 1.0の値を格納
  double v[6];
  double x;

  // 指数関数 a_n = 1 / n!
  for(int I=0; I<6; I++) {
    x = 0.5 + 0.1*I;
    // horner法
    v[I] = an[n-1];
    for(int i=n-2; i>=0; i--) {
      v[I] = v[I]*x + an[i]; // a_k = frac(k)
    }
    // double型小数を表示する
    // 全体桁数25,小数点以下桁数20
    printf("%f, %25.20lf\n", x, v[I]);
  }

  printf("\n");

  // 補間 
  // Nevilleのアルゴリズムを使う
  // x = 0.75の値を求める
  double P[6][6];
  double xj, xk;
  double interpolated;
  double X = 0.75;
  // 初期化 各点の座標を入れておく
  for(int i=0; i<6; i++) {
    /* P[i][0] = v[i]; //f(x_i)を入れる */
    P[i][0] = v[i]; //f(x_i)を入れる
    /* printf("%d, 0, %25.20lf\n", i, P[i][0]); */
  }
  for(int j=1; j<6; j++){
    // ながさj+1
    for(int k=0; k<6-j; k++){
      xj = 0.5 + 0.1*k;
      xk = 0.5 + 0.1*(k+j);
      P[k][j] = ( (X-xk)*P[k][j-1] - (X-xj)*P[k+1][j-1] ) / (xj - xk); 
      /* printf("%d, %d, %25.20lf\n", k, j, P[k][j]); */
    }
  }
  interpolated = P[0][5];
  printf("interpolated: %f, %25.20lf\n", X, interpolated);


  // 誤差の判定
  //
  double exact;
  // horner法
  exact = an[n-1];
  for(int i=n-2; i>=0; i--) {
    exact = exact*X + an[i]; // a_k = frac(k)
  }
  // double型小数を表示する
  // 全体桁数25,小数点以下桁数20
  printf("exact: %f, %25.20lf\n", X, exact);

  // ずれ
  printf("error: %25.20lf\n", interpolated - exact);

}


int main(void) {
  /*
  // 多項式
  for(int n=5; n<=5; n++) {
    for(int I=0; I<6; I++) {
      x = 0.5 + 0.1*I;
      // horner法
      v[I] = 1;
      for(int i=n-1; i>=0; i--) {
        v[I] = v[I]*x + 1; // a_k = 1
      }
    }
  }
  */
  double E[10];
  for(int i=0; i<10; i++) {
    E[i] = 1/frac(i);
    printf("%lf\n", E[i]);
  }
  horner_and_neville(10, E);

  return 0;
}
