import unittest


class Stack:
    def __init__(self, n_max):
        self.array = [0] * n_max
        self.p = -1

    def push(self, val):
        if self.p + 1 >= len(self.array):
            raise RuntimeError('out of range')

        max_val = val
        if self.p >= 0 and max_val < self.array[self.p][1]:
            max_val = self.array[self.p][1]

        self.p += 1
        self.array[self.p] = (val, max_val)

    def peek(self):
        return self.array[self.p][0]

    def pop(self):
        if self.p < 0:
            raise RuntimeError('out of range')

        self.p -= 1
        return self.array[self.p + 1][0]

    def size(self):
        return self.p + 1

    def max(self):
        return self.array[self.p][1]


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


class Queue:
    pass


class TestQueue(unittest.TestCase):
    def test_queue_00(self):
        s = Queue()
        self.assertEqual(0, s.size())
        s.push(8)
        self.assertEqual(8, s.peek())
        self.assertEqual(1, s.size())
        self.assertEqual(8, s.max())
        s.push(5)
        self.assertEqual(8, s.peek())
        self.assertEqual(2, s.size())
        self.assertEqual(8, s.pop())
        self.assertEqual(1, s.size())
        self.assertEqual(5, s.peek())
        self.assertEqual(5, s.max())
        s.push(10)
        self.assertEqual(10, s.max())


if __name__ == '__main__':
    unittest.main()
