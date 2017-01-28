# -*- coding: utf-8 -*-

# Definition for singly-linked list (leetcode)
# ... & some functions to create list of integers from a string
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        rslt = str(self.val)

        while self.next:
            rslt += " -> " + str(self.next.val)
            self = self.next

        return rslt

    def toPythonList(self):
        rslt = [self.val]

        while self.next:
            rslt.append(self.val)

        return rslt

    @staticmethod
    def fromPythonList(xs):
        head = None
        prev = None
        for x in reversed(xs):
            node = ListNode(x)

            if head is None:
                head = node
                prev = node
            else:
                prev.next = node
                prev = node

        return head

    @staticmethod
    def fromString(s, sep=" ", reverse=False):
        """
        :param s:       string, representing the list
        :param sep:     separator string
        :param reverse: pass True if number's most significant digit is the first one in the string

        :return: ListNode for list's head

        Example:
        a = ListNode.fromString('2 4 3')

        `a` will be ListNode { val: 3, next: ListNode { val: 4, next: ListNode { val: 2, next: None}}
        """
        if not isinstance(s, str):
            raise ValueError("String must be passed as a first arguments, {} passed".format(type(s)))

        if not isinstance(sep, str):
            raise ValueError("Separator must be a string, {} passed".format(type(sep)))

        return ListNode.fromPythonList([x for x in s.split(sep) if x])