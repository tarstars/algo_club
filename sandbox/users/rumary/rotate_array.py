#!/usr/bin/python
import unittest


class Solution(object):
    def rotate_simple(self, arr, k):  # O(n*k) - time, O(1) - space
        n = len(arr)
        for i in range(k):
            j = n-1
            temp = arr[n-1]
            while j >= 0:
                arr[j] = arr[j-1]
                j -= 1
            arr[0] = temp
        return arr

    def gcd(self, a, b):  # greatest common divisor
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def rotate_left(self, arr, k):  # juggling algorithm for left rotation
        n = len(arr)                # [1,2,3,4,5] -> [3,4,5,1,2]
        i = 0                       # O(n) - time, O(1) - space
        while i < self.gcd(n, k):
            j = i
            temp = arr[i]
            while True:
                d = (j + k) % n
                if d == i:
                    break
                arr[j] = arr[d]  # move el to the left
                j = d
            arr[j] = temp
            i += 1
        return arr

    def rotate_right(self, arr, k):  # juggling algorithm for right rotation
        n = len(arr)                 # [1,2,3,4,5] -> [4,5,1,2,3]
        i = 0                        # O(n) - time, O(1) - space
        while i < self.gcd(n, k):
            el_to_move = arr[i]
            j = i
            while True:
                d = (j + k) % n
                temp = arr[d]
                arr[d] = el_to_move
                el_to_move = temp
                j = d
                if j == i:
                    break
            i += 1
        return arr


class TestSolution(unittest.TestCase):
    def test_rotate(self):
        s = Solution()
        self.assertEqual([5, 6, 1, 2, 3, 4], s.rotate_simple([1, 2, 3, 4, 5, 6], 2))
        self.assertEqual([3, 99, -1, -100], s.rotate_simple([-1, -100, 3, 99], 2))
        self.assertEqual([4, 5, 6, 7, 1, 2, 3], s.rotate_left([1, 2, 3, 4, 5, 6, 7], 3))
        self.assertEqual([5, 6, 1, 2, 3, 4], s.rotate_right([1, 2, 3, 4, 5, 6], 2))
        self.assertEqual([5, 6, 7, 1, 2, 3, 4], s.rotate_right([1, 2, 3, 4, 5, 6, 7], 3))
        self.assertEqual([3, 99, -1, -100], s.rotate_right([-1, -100, 3, 99], 2))


if __name__ == '__main__':
    unittest.main()
