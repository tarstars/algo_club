from sandbox.users.tarstars.array_structures.main import Stack
import unittest


class MyQueue:

    def __init__(self, n_max):
        self.stack1 = Stack(n_max)
        self.stack2 = Stack(n_max)

    def push(self, val):
        self.stack1.push(val)

    def peek(self):
        if self.stack2.size() > 0:
            return self.stack2.peek()

        self.__moveToStack2__()

        return self.stack2.peek()

    def __moveToStack2__(self):
        for i in range(0, self.stack1.size()):
            element = self.stack1.pop()
            self.stack2.push(element)

    def pop(self):
        if self.stack2.size() > 0:
            return self.stack2.pop()

        self.__moveToStack2__()

        return self.stack2.pop()

    def size(self):
        return self.stack1.size() + self.stack2.size()

    def max(self):
        if self.stack1.max() is None:
            return self.stack2.max()
        if self.stack2.max() is None:
            return self.stack1.max()

        return max(self.stack1.max(), self.stack2.max())


class TestQueue(unittest.TestCase):
    def test_queue_00(self):
        s = MyQueue(10)
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

    def test_queue_01(self):
        q = MyQueue(10)
        q.push(-1)
        self.assertEqual(-1, q.max())


if __name__ == '__main__':
    unittest.main()
