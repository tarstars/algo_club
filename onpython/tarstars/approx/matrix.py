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

    def __repr__(self):
        return "Matrix({!r})".format(self.dat)            
            
    def width(self):
        return len(self.dat[0])

    def height(self):
        return len(self.dat)

    def get(self, p, q):
        return self.dat[p][q]

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
    
        
