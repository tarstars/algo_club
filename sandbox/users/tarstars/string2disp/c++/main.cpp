#include <iostream>
#include <vector>

class BitMatrix {
public:
  BitMatrix(int h_, int w_) : h(h_), w(w_/8), bytes(h*w) {}
  bool Get(int p, int q) const {return (bytes[p*w + q/8] & (128>>(q%8))) != 0;}
  size_t Height() const {return h;}
  size_t Width() const {return w*8;}
  void Set(int p, int q, bool val) {
    unsigned char &current_byte = bytes[p*w + q/8];
    unsigned char mask = 128 >> (q % 8);
    if (val) {
      current_byte |= mask;
    } else {
      current_byte &=  ~mask;
    }
  }
  unsigned char * GetBuffer() {return &bytes[0];}
private:
  size_t h, w;
  std::vector<unsigned char> bytes;
};

BitMatrix LoadFromDotMinus(size_t h, size_t w, std::istream& is) {
  BitMatrix result(h, w);
  for (int p = 0; p < h; ++p) {
    for (int q = 0; q < w; ++q) {
      char current_point;
      is >> current_point;
      if (current_point == '*' || current_point == '-') {
	result.Set(p, q, true);
      } else if (current_point != '.') {
	throw(std::domain_error("unknown symbol in bitfield specification"));
      }
    }
  }
  return result;
}

std::ostream&
SaveAsDotMinus(std::ostream& os, const BitMatrix& bm) {
  for (int p = 0; p < bm.Height(); ++p) {
    for (int q = 0; q < bm.Width(); ++q) {
      if (bm.Get(p, q)) {
	os << "-";
      } else {
	os << ".";
      }
    }
    os << std::endl;
  }
  return os;
}

void
BruteForceFill(BitMatrix *buffer, int ltx, int lty, int rw, int rh, bool set_to_one) {
  for (int p = lty; p < lty + rh; ++p) {
    for (int q = ltx; q < ltx + rw; ++q) {
      buffer->Set(p, q, set_to_one);
    }
  }
}

void
NiceFill(unsigned char *buffer, int w, int ltx, int lty, int rw, int rh, bool filler) {
  if (ltx%8 != 0) {
    unsigned char left_mask = 0;
    for (int p = std::max(0, ltx % 8 - rw); p < ltx % 8; --p) {
      left_mask |= 128 >> p;
    }
    for (int p = lty; p <= lty + rh; ++p) {
      if (filler) {
	buffer[p*w + ltx/8] |= left_mask;
      } else {
	buffer[p*w + ltx/8] &= ~left_mask;
      }
    }
  }
  if ((ltx + rw) %8 != 0 && ltx / 8 != (ltx + rw) / 8) {
    unsigned char right_mask = 0;
    for (int p = ltx % 8; p > std::max(-1, ltx % 8 - rw); --p) {
      right_mask |= 128 >> p;
    }
    for (int p = lty; p <= lty + rh; ++p) {
      if (filler) {
	buffer[p*w + ltx/8] |= right_mask;
      } else {
	buffer[p*w + ltx/8] &= ~right_mask;
      }
    }
  }

}

int main() {
  size_t h, w;
  int ltx, lty, rh, rw;
  int set_to_it;
  std::cin >> w >> h;
  std::cin >> ltx >> lty >> rw >> rh;
  std::cin >> set_to_it;
  BitMatrix BitField = LoadFromDotMinus(h, w, std::cin);
  NiceFill(BitField.GetBuffer(), BitField.Width(), ltx, lty, rw, rh, set_to_it == 1);
  SaveAsDotMinus(std::cout, BitField);
  return 0;
}
