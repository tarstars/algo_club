# -*- coding: utf-8 -*-

from list import ListNode


class Solution(object):
    def addTwoNumbersFromStdin(self, l1, l2):
        return self.addTwoNumbers(ListNode.fromString(l1), ListNode.fromString(l2))

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        cur_val = 0
        mod = 0
        node = ListNode(None)
        head = node
        rest = None

        while True:
            cur_val = l1.val + l2.val + mod

            if cur_val >= 10:
                mod = 1
                cur_val -= 10
            else:
                mod = 0

            node.next = ListNode(cur_val)
            node = node.next

            if l1.next is None:
                rest = l2.next
                break

            if l2.next is None:
                rest = l1.next
                break

            l1 = l1.next
            l2 = l2.next

        while rest is not None:
            cur_val = rest.val + mod

            if cur_val >= 10:
                mod = 1
                cur_val -= 10
            else:
                mod = 0

            node.next = ListNode(cur_val)
            node = node.next
            rest = rest.next

        if mod == 1:
            node.next = ListNode(1)

        return head.next  # leetcode
