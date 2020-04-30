import unittest
from stack_on_array import Stack


class Queue:
    def __init__(self, n):
        self.stack_push = Stack(n)
        self.stack_pop = Stack(n)

    def enqueue(self, val): # queue push
        self.stack_push.push(val)

    def dequeue(self):      # queue pop
        if self.stack_pop.size() == 0:
            while self.stack_push.size() != 0:
                self.stack_pop.push(self.stack_push.pop())
            return self.stack_pop.pop()
        return self.stack_pop.pop()

    def peek(self):
        if self.stack_pop.size() == 0:
            while self.stack_push.size() != 0:
                self.stack_pop.push(self.stack_push.pop())
            return self.stack_pop.peek()
        return self.stack_pop.peek()

    def size(self):
        return self.stack_pop.size() + self.stack_push.size()

    def max(self):
        return max(self.stack_pop.max(), self.stack_push.max())


class TestQueue(unittest.TestCase):
    def test_queue_00(self):
        s = Queue(10)
        self.assertEqual(0, s.size())
        s.enqueue(8)
        self.assertEqual(8, s.peek())
        self.assertEqual(1, s.size())
        self.assertEqual(8, s.max())
        s.enqueue(5)
        self.assertEqual(8, s.peek())
        self.assertEqual(2, s.size())
        self.assertEqual(8, s.dequeue())
        self.assertEqual(1, s.size())
        self.assertEqual(5, s.peek())
        self.assertEqual(5, s.max())
        s.enqueue(10)
        self.assertEqual(10, s.max())


if __name__ == '__main__':
    unittest.main()