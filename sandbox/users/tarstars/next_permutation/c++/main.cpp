#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int val;
  std::vector<int> permut;
  while(std::cin >> val) {
    permut.push_back(val);
  }

  std::next_permutation(permut.begin(), permut.end());

  for (int val : permut) {
    std::cout << val << " ";
  }

  return 0;
}
