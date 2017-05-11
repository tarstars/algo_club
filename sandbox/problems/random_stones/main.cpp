#include <iostream>
#include <random>

class Rnd {
public:
  Rnd():distribution(0,2) {}
  int operator()(void) {
    return distribution(generator);
  }
private:
  std::default_random_engine generator;
  std::uniform_int_distribution<int> distribution;
};

class Matrix {
public:
  Matrix(int h_, int w_) : h(h_), w(w_), dat(h_ * w_) {}
  std::vector<int>::iterator
  operator[](int p) {return dat.begin() + w * p;}
  std::vector<int>::const_iterator
  operator[](int p) const {return dat.begin() + w * p;}
  size_t width() const {return w;}
  size_t height() const {return h;}
private:
  size_t h, w;
  std::vector<int> dat;
};

std::ostream&
operator<<(std::ostream& os, const Matrix& mat) {
  size_t h = mat.height();
  size_t w = mat.width();
  for(int p = 0; p < h; ++p) {
    for(int q = 0; q < w; ++q) {
      os << mat[p][q] << " ";
    }
    os << std::endl;
  }
  return os;
}

Matrix
create_no_extinct_field(size_t h, size_t w);

bool
is_good_field(const Matrix & mat);

Matrix
create_good_field(size_t h, size_t w) {
  while(true) {
    Matrix result = create_no_extinct_field(h, w);
    if (is_good_field(result)) {
      return result;
    }
  }
}

Matrix
create_no_extinct_field(size_t h, size_t w) {
  Rnd rnd;
  Matrix result(h, w);
  for(size_t p = 0; p < h; ++p) {
    for(size_t q = 0; q < w; ++q) {
      do {
        result[p][q] = rnd();
      } while ( (p > 1 && result[p][q] == result[p - 1][q] && result[p][q] == result[p - 2][q]) ||
                (q > 1 && result[p][q] == result[p][q - 1] && result[p][q] == result[p][q - 2]));
    }
  }
  return result;
}

bool
is_good_field(const Matrix & mat) {
  size_t h = mat.height();
  size_t w = mat.width();

  std::vector<std::string> nice_figures = {
    "100011",
    "001110",
    "011100",
    "110001",
    "010101",
    "101010"
  };

  for (size_t p = 0; p < h - 1; ++p) {
    for (size_t q = 0; q < w - 2; ++q) {
      for (size_t fi = 0; fi < nice_figures.size(); ++fi) {
        bool first = false;
        char color = 0;
        bool good = true;
        for (size_t pp = 0; pp < 2; ++pp) {
          for (size_t qq = 0; qq < 3; ++qq) {
            if (nice_figures[fi][pp*3 + qq] == '1') {
              if (first) {
                first = false;
                color = mat[p + pp][q + qq];
              } else {
                if (color != mat[p + pp][q + qq]) {
                  good = false;
                }
              }
            }
          }
        }
        if (good) {
          return true;
        }
      }
    }
  }
  
  return false;
}


int main() {
  auto mat = create_good_field(20, 10);
  std::cout << mat << std::endl;
  return 0;
}
