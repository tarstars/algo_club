#include <iostream>
#include <stdlib.h>


class Matrix {
public:
    Matrix(int h, int w): h(h), w(w), data((int*)malloc(sizeof(int)*h*w)) {
        for (int p = 0; p < h; ++p) {
            for (int q = 0; q < w; ++q) {
                set(p, q, 0);
            }
        }
        printf("%d\n", h);
        printf("%lu\n", sizeof(int)*h*w);
        printf("%p\n", malloc(sizeof(int)*h*w));
        printf("%pd\n", (int*)malloc(sizeof(int)*h*w));
    }

    void set(int p, int q, int val) {data[p*w + q] = val;}

    int get(int p, int q) {return data[p*w + q];}

    int* multiply(Matrix b, Matrix c, int wb) {
        int result_item = 0;

        for (int p = 0; p < this -> h; ++p) {
            for (int q = 0; q < wb; ++q) {
                for (int r = 0; r < this -> w; r++){
                    result_item += this -> data[p*w + r] * b.data[r*wb + q];
                }
                c.data[p*wb + q] = result_item;
                result_item = 0;
            }
        }
        return c.data;
    }

    ~Matrix() {free(data);}

private:
    int h, w;
    int *data;
};

int main(){
    int h1, w1, h2, w2;
    std::cout << "Please, enter size of your **first** matrix:";
    std::cin >> h1 >> w1;

    std::cout << "Please, enter size of your **second** matrix:";
    std::cin >> h2 >> w2;

    Matrix a(h1, w1), b(h2, w2), c(h1, w2);

    std::cout << "Please, fill some elements in format <row_index> <columns_index> <value> => " << std::endl;
    std::cout << "First Matrix => " << std::endl;

    int p, q, v;
    while (std::cin >> p >> q >> v) {
        a.set(p, q, v);
    }
    std::cout << std::endl;
    std::cout << "Your matrix is" << std::endl;

    for (int p = 0; p < h1; ++p) {
        for (int q = 0; q < w1; ++q) {
            std::cout << a.get(p, q) << "\t";
        }
        std::cout << std::endl;
    }

    std::cout << "Second Matrix => " << std::endl;
    while (std::cin >> p >> q >> v) {
        b.set(p, q, v);
    }
    std::cout << std::endl;
    std::cout << "Your matrix is" << std::endl;

    for (int p = 0; p < h2; ++p) {
        for (int q = 0; q < w2; ++q) {
            std::cout << b.get(p, q) << "\t";
        }
        std::cout << std::endl;
    }

    a.multiply(b, c, w2);
    for (int p = 0; p < h1; ++p) {
        for (int q = 0; q < w2; ++q) {
            std::cout << c.get(p, q) << "\t";
        }
        std::cout << std::endl;
    }

    return 0;
}
