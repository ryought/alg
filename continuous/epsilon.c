#include <stdio.h>

// マシンイプシロンを求めようとする試み
int main(int argc, char *argv[]) {
  double x = 1;
  double prev_x = x*2;
  int i = 0;
  printf("%f\n", x/2);

  while(x != 0) {
    prev_x = x;
    x = x/2;
    i++;
    printf("%e(in %d)\n", x, i);
  }


  

  return 0;
}
