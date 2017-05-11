#include <iostream>
#include <vector>

class Display {
public:
  Display(size_t h_, size_t w_) : h(h_), w(w_), dat(h_ * w_/8, 0) {}
  void print(std::ostream &) const;

  std::vector<uint8_t>::iterator
  operator[](int ind) {return dat.begin() + w / 8 * ind;}

  std::vector<uint8_t>::const_iterator
  operator[](int ind) const {return dat.begin() + w / 8 * ind;}

  void set(int p, int q, uint8_t color) {
    uint8_t &element = (*this)[p][q / 8];
    if (color) {
      element |= 128 >> (q % 8);
    } else {
      element &= ~(128 >> (q % 8));
    }
  }

  size_t width() const {return w;}
  size_t height() const {return h;}
  
  uint8_t *get_raw() {
    return &dat[0];
  }
  
private:
  size_t h, w;
  std::vector<uint8_t> dat;
};

std::ostream&
operator<< (std::ostream& os, const Display &disp) {
  disp.print(os);
  return os;
}


void
Display::print(std::ostream &os) const {
  for (size_t p = 0; p < h; ++p) {
    for(size_t q = 0; q < w / 8; ++q) {
      for(size_t qq = 0; qq < 8; ++qq) {
        if ((*this)[p][q] & (128 >> qq)) {
          os << "*";
        } else {
          if (qq == 0) {
            os << ";";
          } else {
            os << ".";
          }
        }
      }
    }
    os << std::endl;
  }
}     


void rectangle(uint8_t *pbuf, int w, int ltx, int lty, int rbx, int rby, int color) {
  uint8_t mm = 0;
  uint8_t lm = 0, rm = 0;

  int left_byte_pos = ltx / 8;
  int right_byte_pos = rbx / 8;

  if (left_byte_pos == right_byte_pos) {
    for (int ind = ltx % 8; ind <= rbx % 8; ++ind) {
      mm |= 128 >> ind;
    }
    if (!color) {
      mm = ~mm;
    }
  } else {
    for (int ind = ltx % 8; ind < 8; ++ind) {
      lm |= 128 >> ind;
    }
    for (int ind = 0; ind < rbx % 8; ++ind) {
      rm |= 128 >> ind;
    }
    if (!color) {
      lm = ~lm;
      rm = ~rm;
    }
  }

  for (int p = lty; p <= rby; ++p) {
    if (left_byte_pos == right_byte_pos) {
      uint8_t &element = pbuf[p * (w / 8) + left_byte_pos];
      if (color) {
        element |= mm;
      } else {
        element &= mm;
      }
    } else {
      uint8_t &left_element = pbuf[p * (w / 8) + left_byte_pos];
      uint8_t &right_element = pbuf[p * (w / 8) + right_byte_pos];

      if (color) {
        left_element |= lm;
        right_element |= rm;
      } else {
        left_element &= lm;
        right_element &= rm;
      }

      for (int ind = left_byte_pos + 1; ind < right_byte_pos; ++ind) {
        pbuf[p * (w / 8) + ind] = 255 * color;
      }
    }
  }
}


int main() {
  Display pic(46, 60);

  for (int p = 0; p < pic.height(); ++p) {
    for (int q = 0; q < pic.width(); ++q) {
      int dp = p - 8;
      int dq = q - 8;
      if (dp * dp + dq * dq < 49) {
        pic.set(p, q, 1);
      }
    }
  }

  rectangle(pic.get_raw(), pic.width(), 20, 2, 22, 6, 1);
  rectangle(pic.get_raw(), pic.width(), 20, 8, 35, 16, 1);
  rectangle(pic.get_raw(), pic.width(), 6, 20, 36, 40, 1);
  rectangle(pic.get_raw(), pic.width(), 14, 25, 30, 35, 0);
  
  std::cout << pic << std::endl;
  return 0;
}
