#include <stdio.h>
/*
 * 行列乗算C = ABを計算する
 * 
 */

// A[n][m], B[m][l] から C[n][l] を計算
void mult_matrix(int n, int m, int l, double C[n][l], double A[n][m], double B[m][l]) {
  for(int i=0; i<n; i++) {
    for(int j=0; j<l; j++) {
      C[i][j] = 0;
      for(int k=0; k<m; k++) 
        C[i][j] = C[i][j] + (A[i][k] * B[k][j]);
    }
  }
}

void print_matrix(int n, int m, double A[n][m]) {
  for (int i=0; i<n; i++) {
    for (int j=0; j<m; j++) {
      printf(" %f ", A[i][j]);
    }
    printf("\n");
  }
}

// Strassen algorithm で O(N^{log_2 7}) で計算
void mult_matrix_fast(int n, int m, int l, 
                      double C[n][l], double A[n][m], double B[m][l]) {
}

int main(int argc, char *argv[]) {

  double A[2][3] = {{1,2,3},
                    {5,3,4}};
  double B[3][2] = {{5,3},
                    {8,2},
                    {7,4}};

  double C[2][2] = {{0,0},
                    {0,0}};

  print_matrix(2, 2, C);
  mult_matrix(2, 3, 2, C, A, B);
  print_matrix(2, 2, C);

  return 0;
}
