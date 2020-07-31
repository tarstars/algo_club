import unittest


class Stack:
    def __init__(self, n):
        self.array = [[0, 0]] * n
        self.p = 0

    def push(self, val):
        if self.p >= len(self.array):
            raise RuntimeError('Out of range')

        max_val = val
        if self.p > 0 and max_val < self.array[self.p-1][1]:
            max_val = self.array[self.p-1][1]

        self.array[self.p] = [val, max_val]
        self.p += 1

    def peek(self):
        if self.p == 0:
            raise RuntimeError('stack is empty')
        return self.array[self.p - 1][0]

    def pop(self):
        if self.p == 0:
            raise RuntimeError('stack is empty')
        self.p -= 1
        return self.array[self.p][0]

    def size(self):
        return self.p

    def max(self):
        if self == 0:
            return None
        return self.array[self.p - 1][1]


class TestStack(unittest.TestCase):
    def test_stack_00(self):
        s = Stack(10)
        self.assertEqual(0, s.size())
        s.push(8)
        self.assertEqual(8, s.peek())
        self.assertEqual(1, s.size())
        self.assertEqual(8, s.max())
        s.push(5)
        self.assertEqual(5, s.peek())
        self.assertEqual(2, s.size())
        self.assertEqual(5, s.pop())
        self.assertEqual(1, s.size())
        self.assertEqual(8, s.peek())
        self.assertEqual(8, s.max())
        s.push(10)
        self.assertEqual(10, s.max())


if __name__ == '__main__':
    unittest.main()
