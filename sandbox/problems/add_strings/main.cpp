#include <iostream>
#include <string>

std::string
add(const std::string &a,
    const std::string &b) {
  size_t n = std::max(a.size(), b.size()) + 1;
  std::string ret(n, ' ');
  int c = 0;
  for (size_t q = 0; q < n; ++q) {
    if (q < a.size()) {
      c += a[a.size() - 1 - q] - '0';
    }
    if (q < b.size()) {
      c += b[b.size() - 1 - q] - '0';
    }
    ret[n - 1 - q] = '0' + c % 10;
    c /= 10;
  }
  if (ret[0] == '0') {
    ret = ret.substr(1, ret.size() - 1);
  }
  return ret;
}

void testcase(const std::string &a,
	      const std::string &b,
	      const std::string &c) {
  std::string val = add(a, b);
  if (val == c) {
    std::cout << "OK" << std::endl;
  } else {
    std::cout << "FAIL: " << val << std::endl;
  }
}

int main() {
  testcase("123", "44", "167");
  testcase("9", "1", "10");
  testcase("999", "1", "1000");
  testcase("989", "1", "990");

  return 0;
}
