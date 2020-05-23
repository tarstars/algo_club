import unittest


# 5:36 - 6:05 -

class ListNode:
    def __init__(self, val=None):
        self.next = None
        self.val = val


def iter2list(it):
    head = None
    tail = None
    for val in it:
        if head is None:
            head = ListNode(val=val)
            tail = head
        else:
            new_tail = ListNode(val=val)
            tail.next = new_tail
            tail = new_tail
    return head


def list2array(head):
    def list_iter(head):
        while head is not None:
            yield head.val
            head = head.next

    return list(list_iter(head=head))


# 3:16 - 3:27 - 3:30

def k_group_reverse(lst, k):
    n = 0
    it = lst
    while it:
        n += 1
        it = it.next

    if n < 2 or k < 2:
        return lst

    number_of_chunks = n // k
    if number_of_chunks == 0:
        return lst

    begin_of_result = None
    end_of_result = None
    begin_of_rest = lst
    for _ in range(number_of_chunks):
        head_of_inverse = begin_of_rest
        tail_of_inverse = begin_of_rest
        begin_of_rest = begin_of_rest.next
        for _ in range(k - 1):
            next_begin_of_rest = begin_of_rest.next
            begin_of_rest.next = head_of_inverse
            head_of_inverse = begin_of_rest
            begin_of_rest = next_begin_of_rest
        if begin_of_result is None:
            begin_of_result = head_of_inverse
            end_of_result = tail_of_inverse
        else:
            end_of_result.next = head_of_inverse
            end_of_result = tail_of_inverse
    end_of_result.next = begin_of_rest

    return begin_of_result


class TestKGroup(unittest.TestCase):
    def test_kgroup_00(self):
        my_list = iter2list(range(10))
        mutated_list = k_group_reverse(my_list, 4)
        self.assertEqual([3, 2, 1, 0, 7, 6, 5, 4, 8, 9], list2array(mutated_list))
