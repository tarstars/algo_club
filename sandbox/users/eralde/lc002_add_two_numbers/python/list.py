# -*- coding: utf-8 -*-

# Definition for singly-linked list (leetcode)
# ... & some functions to create list of integers from a string
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def _print(self, sep):
        if not isinstance(sep, str):
            raise ValueError("Separator must be a string, {} passed".format(type(sep)))

        return sep.join(map(str, self.toPythonList()))

    def __str__(self):
        return self._print(' ')

    def prettyPrint(self):
        return self._print(' -> ')

    def toPythonList(self):
        rslt = [self.val]
        cur = self.next

        while cur:
            rslt.append(cur.val)
            cur = cur.next

        return rslt

    @staticmethod
    def fromPythonList(xs):
        head = None
        prev = None

        for x in list(map(int, xs)):
            node = ListNode(x)

            if head is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        return head

    @staticmethod
    def fromString(s, sep=" "):
        """
        :param s:       string, representing the list
        :param sep:     separator string
        :return: ListNode for list's head

        Example:
        a = ListNode.fromString('2 4 3')

        `a` will be ListNode { val: 3, next: ListNode { val: 4, next: ListNode { val: 2, next: None}}
        """
        if not isinstance(s, str):
            raise ValueError("String must be passed as a first arguments, {} passed".format(type(s)))

        if not isinstance(sep, str):
            raise ValueError("Separator must be a string, {} passed".format(type(sep)))

        return ListNode.fromPythonList(s.strip().split(sep))
