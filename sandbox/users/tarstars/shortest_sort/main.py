#!/usr/bin/env python2

import unittest


def shortest(nums):
    if len(nums) < 2:
        return 0

    # left to right
    maxv = nums[0]
    right_best = 0
    for ind in range(1, len(nums)):
        if maxv > nums[ind]:
            right_best = ind
        else:
            maxv = nums[ind]

    if right_best == 0:
        return 0

    # right to left
    minv = nums[-1]
    left_best = len(nums) - 1
    for ind in range(len(nums) - 1, -1, -1):
        if minv < nums[ind]:
            left_best = ind
        else:
            minv = nums[ind]

    return right_best - left_best + 1


class TestShortestSort(unittest.TestCase):
    def test_short(self):
        self.assertEqual(shortest([1]), 0)

    def test_two_00(self):
        self.assertEqual(shortest([1, 2]), 0)

    def test_two_01(self):
        self.assertEqual(shortest([2, 1]), 2)

    def test_many_00(self):
        self.assertEqual(shortest([1, 2, 4, 5, 6, 3, 7, 8, 9, 10]), 4)

    def test_many_01(self):
        self.assertEqual(shortest([1, 2, 8, 4, 5, 6, 7, 3, 9, 10]), 6)

    def test_many_02(self):
        self.assertEqual(shortest([1, 2, 3, 4, 5, 7, 6, 8, 9, 10]), 2)

    def test_many_03(self):
        self.assertEqual(shortest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 0)

    def test_many_04(self):
        self.assertEqual(shortest([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]), 2)

    def test_many_05(self):
        self.assertEqual(shortest([1, 2, 3, 4, 5, 6, 7, 8, 10, 9]), 2)

    def test_many_06(self):
        self.assertEqual(shortest([5, 4, 3, 2, 1]), 5)

    def test_many_07(self):
        self.assertEqual(shortest([2, 3, 2, 3, 3, 3]), 2)

    def test_many_08(self):
        self.assertEqual(shortest([1, 3, 2, 3, 3]), 2)


if __name__ == '__main__':
    unittest.main()
