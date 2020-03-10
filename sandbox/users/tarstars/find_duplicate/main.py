import unittest
from typing import List


class TestFindDuplicate(unittest.TestCase):
    def test_find_duplicate_00(self):
        self.assertEqual(2, find_duplicate([1, 2, 2]))

    def test_find_duplicate_01(self):
        self.assertEqual(1, find_duplicate([1, 1, 2]))


def find_duplicate(nums: List[int]) -> int:
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
