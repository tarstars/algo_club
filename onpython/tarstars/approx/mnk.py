#!/usr/bin/env python3

import matrix
import unittest

def create_mnk_matrix(dat):
    max_order = 10
    order = min(max_order, len(dat)-1)
    dat = matrix.Matrix.matrix_like_init(dat)
    b = matrix.Matrix.shape_init(dat.height(), order + 1)
    y = matrix.Matrix.shape_init(dat.height(), 1)
    for p in range(dat.height()):
        for q in range(order+1):
            b.set(p, q, float(dat.get(p, 0))**q)
        y.set(p, 0, float(dat.get(p, 1)))
    return b, y


class TestCreateMnkMatrix(unittest.TestCase):
    def test_create_mnk_matrix_00(self):
        dat = [(0, 0), (1, 1)]
        b, y = create_mnk_matrix(dat)
        self.assertEqual(b, matrix.Matrix.matrix_like_init([[1, 0], [1, 1]]))
        self.assertEqual(y, matrix.Matrix.matrix_like_init([[0], [1]]))


if __name__ == '__main__':
    unittest.main()
