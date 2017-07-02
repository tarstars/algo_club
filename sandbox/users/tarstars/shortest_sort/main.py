#!/usr/bin/env python2

import unittest


def shortest(nums):
    if len(nums) < 2:
        return 0

    # left boundary
    l = None
    for l in range(len(nums)):
        if l < len(nums) - 1 and nums[l] > nums[l + 1]:
            break

    if l == len(nums) - 1:
        return 0
        
    rest_min = min(nums[l + 1:])

    lb = None
    for lb in range(l, -1, -1):
        if nums[lb] <= rest_min:
            break

    # right boundary
    r = None
    for r in range(len(nums) - 1, 0, -1):
        if nums[r - 1] > nums[r]:
            break


    rest_max = max(nums[:r])

    rb = None
    for rb in range(len(nums) - 1, r - 1, -1):
        if nums[rb] <= rest_max:
            break

    if nums[0] > nums[1] and nums[-2] > nums[-1]:
        return len(nums)

    ret = rb - lb

    if ret < 2:
        ret = 2

    return ret


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


if __name__ == '__main__':
    unittest.main()
