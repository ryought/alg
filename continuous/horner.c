#include <stdio.h>

double frac(int n) {
  double r = 1;
  for(int i=1; i<=n; i++){
    r = r*(double)i;
  }
  return r;
}

int main(int argc, char *argv[]) {
  // x = 0.5 - 1.0の値を格納
  double v[6];
  double x;


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
    printf("%d: %f, %f, %f, %f, %f, %f\n", n, v[0], v[1], v[2], v[3], v[4], v[5]);
  }

  // 指数関数 a_n = 1 / n!
  double exp[6];
  int n = 10;
  for(int I=0; I<6; I++) {
    x = 0.5 + 0.1*I;
    // horner法
    exp[I] = 1/frac(n);
    for(int i=n-1; i>=0; i--) {
      exp[I] = exp[I]*x + 1/frac(i); // a_k = frac(k)
    }
    printf("exp(%f) = %f\n", x, exp[I]);
  }

  // 補間 
  // Nevilleのアルゴリズムを使う
  // x = 0.75の値を求める
  double P[6][6];
  double xj, xk;
  x = 0.75;
  // 初期化 各点の座標を入れておく
  for(int i=0; i<6; i++) {
    /* P[i][0] = v[i]; //f(x_i)を入れる */
    P[i][0] = exp[i]; //f(x_i)を入れる
    printf("%f\n", P[i][0]);
  }
  for(int j=1; j<6; j++){
    // ながさj+1
    for(int k=0; k<6-j; k++){
      xj = 0.5 + 0.1*k;
      xk = 0.5 + 0.1*(k+j);
      P[k][j] = ( (x-xk)*P[k][j-1] - (x-xj)*P[k+1][j-1] ) / (xj - xk); 
    }
  }
  printf("%f\n", P[0][5]);
  
  return 0;
}
