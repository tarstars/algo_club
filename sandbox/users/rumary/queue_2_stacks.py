import unittest
from stack_on_array import Stack


class Queue:
    def __init__(self, n):
        self.stack_push = Stack(n)
        self.stack_pop = Stack(n)

    def move_to_pop_stack(self):
        while self.stack_push.size() != 0:
            self.stack_pop.push(self.stack_push.pop())

    def enqueue(self, val):  # queue push
        self.stack_push.push(val)

    def dequeue(self):       # queue pop
        if self.stack_pop.size() == 0:
            self.move_to_pop_stack()
        return self.stack_pop.pop()

    def peek(self):
        if self.stack_pop.size() == 0:
            self.move_to_pop_stack()
        return self.stack_pop.peek()

    def size(self):
        return self.stack_pop.size() + self.stack_push.size()

    def max(self):
        if self.stack_pop.size() == 0:
            return self.stack_push.max()
        else:
            return max(self.stack_pop.max(), self.stack_push.max())


class TestQueue(unittest.TestCase):
    def test_queue_00(self):
        s = Queue(10)
        s.enqueue(-1)
        print s.max()
        self.assertEqual(-1, s.max())
        self.assertEqual(1, s.size())
        s.enqueue(8)
        self.assertEqual(-1, s.peek())
        self.assertEqual(2, s.size())
        self.assertEqual(8, s.max())
        s.enqueue(5)
        self.assertEqual(-1, s.peek())
        self.assertEqual(3, s.size())
        self.assertEqual(-1, s.dequeue())
        self.assertEqual(2, s.size())
        self.assertEqual(8, s.peek())
        self.assertEqual(8, s.max())
        s.enqueue(10)
        self.assertEqual(10, s.max())


if __name__ == '__main__':
    unittest.main()
