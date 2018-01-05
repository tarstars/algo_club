#!/usr/bin/env python3

import matrix

import math
import mnk
import unittest


def gauss_solve(a, y):
    n = a.width()
    x = matrix.Matrix.shape_init(n, 1)
    for pos in range(n-1):
        maxel_ind = pos
        maxel = math.fabs(a.get(pos,pos))
        for ind in range(pos+1, n):
            if maxel < math.fabs(a.get(ind, pos)):
                maxel = math.fabs(a.get(ind, pos))
                maxel_ind = ind

        if maxel_ind != pos:
            for temp_ind in range(pos, n):
                temp_val = a.get(maxel_ind, temp_ind)
                a.set(maxel_ind, temp_ind, a.get(pos, temp_ind))
                a.set(pos, temp_ind, temp_val)
            temp_val = y.get(pos, 0)
            y.set(pos, 0, y.get(maxel_ind, 0))
            y.set(maxel_ind, 0, temp_val)

        for victim in range(pos+1, n):
            magic = a.get(victim, pos)/a.get(pos, pos)
            y.set(victim, 0, y.get(victim, 0) - y.get(pos, 0)*magic)
            for subvictim in range(pos, n):
                a.set(victim, subvictim, a.get(victim, subvictim) - a.get(pos, subvictim)*magic)

    x.set(n-1, 0, y.get(n-1, 0)/a.get(n-1, n-1))
    for pos in range(n-2, -1, -1):
        right = y.get(pos, 0)
        for p in range(pos+1, n):
            right -= x.get(p, 0)*a.get(pos, p)
        x.set(pos, 0, right/a.get(pos, pos))
    return x


class TestGaussSolve(unittest.TestCase):
    def test_ordinary_case_00(self):
        a = matrix.Matrix.matrix_like_init([[1, 0], [0, 1]])
        y = matrix.Matrix.matrix_like_init([[3], [5]])
        x = gauss_solve(a, y)
        self.assertTrue(x.almost_equal(matrix.Matrix.matrix_like_init([[3], [5]])))

    def test_ordinary_case_01(self):
        a = matrix.Matrix.matrix_like_init([[0, 1], [1, 0]])
        y = matrix.Matrix.matrix_like_init([[5], [3]])
        x = gauss_solve(a, y)
        self.assertTrue(x.almost_equal(matrix.Matrix.matrix_like_init([[3], [5]])))

    def test_ordinary_case_02(self):
        a = matrix.Matrix.matrix_like_init([[1, 1], [1, -1]])
        y = matrix.Matrix.matrix_like_init([[8], [2]])
        x = gauss_solve(a, y)


class TestGaussianApproximator(unittest.TestCase):
    def test_approximator_00(self):
        points = [(-2.77, -0.67), (-1.08, 0.4), (0.63, 0.83), (2.06, 0.25)]
        b, y = mnk.create_mnk_matrix(points)
        expected_b = matrix.Matrix([[1.0, -2.77, 7.6729, -21.253933],
                                  [1.0, -1.08, 1.1664, -1.2597120000000002],
                                  [1.0, 0.63, 0.39690000000000003, 0.250047],
                                  [1.0, 2.06, 4.2436, 8.741816]])
        self.assertTrue(b.almost_equal(expected_b), '{} is not equal to {}'.format(b, expected_b))

        expected_y = matrix.Matrix([[-0.67], [0.4], [0.83], [0.25]])
        self.assertTrue(y.almost_equal(expected_y), '{} is not equal to {}'.format(y, expected_y))


if __name__ == '__main__':
    unittest.main()