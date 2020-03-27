import unittest
from typing import List


class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate_00(self):
        self.assertEqual(find_duplicate([1, 2, 2]), 2)

    def test_find_duplicate_01(self):
        self.assertEqual(find_duplicate([1, 1, 2]), 1)


def binary_search(a, b, p):
    while b - a > 1:
        m = (a + b) // 2
        if p(m):
            b = m
        else:
            a = m
    return b


def find_duplicate(nums: List[int]) -> int:
    def contains_extra(v):
        return sum(1 for vv in nums if vv <= v) > v

    return binary_search(0, len(nums), contains_extra)


def find_duplicate_digits(nums: List[int]) -> int:
    md = 32
    n = len(nums) - 1

    digs_current = [0] * md
    digs_exemplary = [0] * md

    for ind in range(1, n + 1):
        for dig_ind in range(md):
            digs_exemplary[dig_ind] += 1 if ((1 << dig_ind) & ind) else 0

    for v in nums:
        for dig_ind in range(md):
            digs_current[dig_ind] += 1 if ((1 << dig_ind) & v) else 0

    result = 0
    for di in range(md):
        if digs_current[di] > digs_exemplary[di]:
            result |= (1 << di)

    return result


def find_duplicate_cycle(nums: List[int]) -> int:
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1


if __name__ == '__main__':
    unittest.main()
