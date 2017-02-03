#include <iostream>

int main() {
  int n;
  std::cin >> n;
  int r = 1;
  for (int p = 2; p <= n; ++p) {
    r *= p;
  }
  std::cout << r;
  return 0;
}
