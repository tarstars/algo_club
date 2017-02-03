#!/usr/bin/env python3

class ListNode:
    def __init__(self):
        self.next = None
        self.val = 0

def load_list(s):
    ret = ListNode()
    tail = ret
    for t in s.split():
        if t:
            tail.next = ListNode()
            tail = tail.next
            tail.val = int(t)
            
    return ret.next

def add_list(f, s):
    ret = ListNode()
    tail = ret
    carry = 0
    while True:
        if f:
            carry += f.val
            f = f.next
        if s:
            carry += s.val
            s = s.next
        if carry or f or s:
            tail.next = ListNode()
            tail = tail.next
            tail.val = carry % 10
            carry //= 10
        else:
            break
            
    return ret.next

def print_list(lst):
    while lst:
        print(lst.val)
        lst = lst.next

def main():
    print_list(add_list(load_list(input()), load_list(input())))
    
if __name__ == '__main__':
    main()
