#!/usr/bin/env python3
import copy
import unittest


class Matrix(object):
    def __init__(self, dat):
        if isinstance(dat, Matrix):
            self.dat = copy.deepcopy(dat.dat)
        else:
            self.dat = copy.deepcopy(dat)

    @classmethod
    def vector_init(cls, vec):
        return cls([[t] for t in vec])
            
    @classmethod
    def shape_init(cls, h, w):
        return cls([[0]*w for _ in range(h)])

    @classmethod
    def matrix_like_init(cls, ml_dat):
        return cls([list(t) for t in ml_dat])

    def __repr__(self):
        return "Matrix({!r})".format(self.dat)            
            
    def width(self):
        return len(self.dat[0])

    def height(self):
        return len(self.dat)

    def get(self, p, q):
        return self.dat[p][q]

    def set(self, p, q, val):
        self.dat[p][q] = val

    def transpose(self):
        h, w = self.height(), self.width()
        result = Matrix.shape_init(w, h)
        for p in range(h):
            for q in range(w):
                result.set(q, p, self.get(p, q))
        return result

    def __mul__(self, r):
        res = Matrix.shape_init(len(self.dat), len(r.dat[0]))
        for p in range(len(self.dat)):
            for q in range(len(r.dat[0])):
                val = 0
                for ind in range(len(self.dat[0])):
                    val += self.dat[p][ind] * r.dat[ind][q]
                res.dat[p][q] = val
        return res

    def __eq__(self, other):
        return self.dat == other.dat

    def almost_equal(self, other):
        if (self.width() != other.width() or
            self.height() != other.height()):
            return False

        w = self.width()
        h = self.height()

        s = 0
        for p in range(h):
            for q in range(w):
                d = self.get(p, q) - other.get(p, q)
                s += d**2

        return s < 1e-10

    def first_column_to_list(self):
        return [t[0] for t in self.dat]

    
class TestMatrix(unittest.TestCase):
    def test_matrix_init(self):
        mat = Matrix([[11, 12], [21, 22], [31, 32]])
        self.assertEqual(mat.height(), 3)
        self.assertEqual(mat.width(), 2)
        self.assertEqual(mat.get(2, 1), 32)

    def test_vector_init(self):
        lst = [1, 2, 10, 15]
        mat = Matrix.vector_init(lst)
        self.assertEqual(mat.height(), len(lst))
        self.assertEqual(mat.width(), 1)
        self.assertEqual(mat.get(2, 0), 10)

    def test_shape(self):
        mat = Matrix.shape_init(3, 5)
        self.assertEqual(mat.height(), 3)
        self.assertEqual(mat.width(), 5)

    def test_mat_mul(self):
        a = Matrix([[1, 2],[3, 5]])
        b = Matrix([[-1, 1], [2, 0]])
        c = a * b
        self.assertEqual(c, Matrix([[3, 1], [7, 3]]))

if __name__ == '__main__':
    unittest.main()
    
        
