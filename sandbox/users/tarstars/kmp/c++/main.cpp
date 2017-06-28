#include <iostream>
#include <vector>

struct KMPDescription {
  std::string pat;
  std::vector<int> f;
};

KMPDescription
CreateKMP(std::string pat) {
  std::vector<int> f(pat.size(), -1);
  int pos = -1;
  for (size_t ind = 1; ind < pat.size(); ++ind) {
    while (pos >= 0 && pat[pos] != pat[ind]) {
      pos = f[pos];
    }
    ++pos;
    f[ind] = pos;
  }
  return KMPDescription{pat, f};
}

std::vector<int>
ApplyKMP(const KMPDescription& desc,
         std::string s) {
  int pos = 0;
  std::vector<int> res;
  for (size_t ind = 0; ind < s.size(); ++ind) {
    while (pos >= 0 && desc.pat[pos] != s[ind]) {
      pos = desc.f[pos];
    }
    ++pos;
    if (pos == desc.pat.size()) {
      --pos;
      res.push_back(ind - desc.pat.size() + 1);
      while (pos >= 0 && desc.pat[pos] != s[ind]) {
        pos = desc.f[pos];
      }
    }
  }
  return res;
}

int main() {
  std::string pat, s;
  std::getline(std::cin, pat);
  std::getline(std::cin, s);

  KMPDescription desc = CreateKMP(pat);
  std::vector<int> ans = ApplyKMP(desc, s);

  if (ans.size() == 0) {
    std::cout << "None";
  } else {
    std::cout << ans.front();
    for (size_t p = 1; p < ans.size(); ++p) {
      std::cout << " " << ans[p];
    }
  }
  
  return 0;
}
