import unittest


def count_less(x, v):   # O(n)
    h, w = len(x), len(x[0])
    p, q = 0, w - 1
    s = 0
    while p < h and q > 0:
        while q > 0 and x[p][q - 1] >= v:
            q -= 1
        s += q
        p += 1
    return s


def kth_smallest(x, k):
    a = x[0][0]
    b = x[-1][-1] + 1
    while b - a > 1:
        c = (a + b) // 2
        less_number = count_less(x, c)
        if less_number < k:
            a = c
        else:
            b = c
    return a


class TestLessCount(unittest.TestCase):
    def setUp(self):
        self.mat = [[1, 1, 2, 100],
                    [1, 1, 2, 100],
                    [2, 2, 2, 100],
                    [100, 100, 100, 100]]

        self.mat1 = [[1,5,9],[10,11,13],[12,13,15]]

    def test_00(self):
        self.assertEqual(kth_smallest(self.mat, 1), 1)
        self.assertEqual(kth_smallest(self.mat, 4), 1)

    def test_01(self):
        self.assertEqual(kth_smallest(self.mat, 5), 2)
        self.assertEqual(kth_smallest(self.mat, 9), 2)

    def test_02(self):
        self.assertEqual(kth_smallest(self.mat, 10), 100)
        self.assertEqual(kth_smallest(self.mat, 16), 100)

    def test_03(self):
        self.assertEqual(kth_smallest(self.mat1, 8), 13)




if __name__ == '__main__':
    unittest.main()
