#include <stdio.h>

int main(int argc, char *argv[]) {
  double v1 , v2;  // 速度
  double x1, x2;  // 重心位置
  double r; // 半径(共通)
  // 距離は |x1-x2|-2r
  // 相対速度は |v1-v2|

  // 衝突時刻
  double t = ( abs(x1-x2)-2*r ) / ( abs(v1-v2) );

  printf("t: %f\n", t)

  
  return 0;
}
