#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  int h1 = 3;
  int w1 = 5;
  int *p1 = (int*) malloc(h1 * w1 * sizeof(int));

  p1[0] =  11;  p1[1] = 12;  p1[2] = 13;  p1[3] = 14;  p1[4] = 15;
  p1[5] =  21;  p1[6] = 22;  p1[7] = 23;  p1[8] = 24;  p1[9] = 25;
  p1[10] = 31; p1[11] = 32; p1[12] = 33; p1[13] = 34; p1[14] = 35;

  printf("first matrix is:\n");
  for (int p = 0; p < h1; ++p) {
    for (int q = 0; q < w1; ++q) {
      printf("%d ", p1[p*w1 + q]);
    }
    printf("\n");
  }

  printf("first matrix Transposed is:\n");
  for (int p = 0; p < w1; ++p) {
    for (int q = 0; q < h1; ++q) {
      printf("%d ", p1[q*w1 + p]);
    }
    printf("\n");
  }

  int h2 = 5;
  int w2 = 2;
  int *p2 = (int*) malloc(h2 * w2 * sizeof(int));

  p2[0] =  11;  p2[1] = 12;  p2[2] = 21;  p2[3] = 22;  p2[4] = 31;
  p2[5] =  32;  p2[6] = 41;  p2[7] = 42;  p2[8] = 51;  p2[9] = 52;

  printf("second matrix is:\n");
  for (int p = 0; p < h2; ++p) {
    for (int q = 0; q < w2; ++q) {
      printf("%d ", p2[p*w2 + q]);
    }
    printf("\n");
  }

  printf("second matrix Transposed is:\n");
  for (int p = 0; p < w2; ++p) {
    for (int q = 0; q < h2; ++q) {
      printf("%d ", p2[q*w2 + p]);
    }
    printf("\n");
  }

  int result_item = 0;
  printf("Multiplication of matrixes is:\n");
  for (int p = 0; p < h1; ++p) { // Any variant: w2 == h1 or w2 != h1
    for (int q = 0; q < w2; ++q) {  // h2 == w1
       for (int r = 0; r < w1; r++){
            result_item += p1[p*w1 + r] * p2[r*w2 + q];
            }
            printf("%d ", result_item);
            result_item = 0;
       }
            printf("\n");
  }

  free(p1);
  free(p2);

  return 0;

}

