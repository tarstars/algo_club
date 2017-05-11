#!/usr/bin/python

import unittest
import operator
import functools

def sum_integers(n):
    if n < 1:
        return 0
    return n + sum_integers(n - 1)

    #s = 0
    #ind = 1
    #while True:
    #    if ind > n:
    #        return s
    #    s += ind
    #    ind += 1

    # return n * (n + 1) / 2
    # return sum(range(1, n+1))
    # return functools.reduce(operator.add, range(1, n+1), 0)

class TestSum(unittest.TestCase):
    def test_unit_input(self):
        self.assertEqual(sum_integers(1), 1)

    def test_unit_val_1(self):
        self.assertEqual(sum_integers(5), 15)

    def test_unit_val_2(self):
        self.assertEqual(sum_integers(100), 5050)

    def test_unit_val_3(self):
        self.assertEqual(sum_integers(20), 210)

if __name__ == '__main__':
    unittest.main()
