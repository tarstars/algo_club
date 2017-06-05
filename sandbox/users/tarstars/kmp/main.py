#!/usr/bin/env python3

import unittest

def fibb_str(n):
    a = 'a'
    b = 'b'
    for _ in range(n):
        a, b = b, a + b
    return a

def init_kmp(p):
    pos = -1
    f = [pos] * len(p)
    for ind in range(1, len(p)):
        while pos >= 0 and p[pos] != p[ind]:
            pos = f[pos]
        pos = pos + 1
        f[ind] = pos
    return (str(p), f)


class TestInitKMP(unittest.TestCase):
    def test_simple_string_00(self):
        self.assertEqual(init_kmp('aaaa')[1], [-1, 0, 1, 2])

    def test_simple_string_01(self):
        self.assertEqual(init_kmp('')[1], [])

    def test_simple_string_02(self):
        self.assertEqual(init_kmp('a')[1], [-1])
        
    def test_simple_string_03(self):
        self.assertEqual(init_kmp('aba')[1], [-1, 0, 1])

    def test_simple_string_04(self):
        self.assertEqual(init_kmp('abac')[1], [-1, 0, 1, 0])

    def test_simple_string_05(self):
        self.assertEqual(init_kmp('aab')[1], [-1, 0, 0])

    def test_simple_string_06(self):
        self.assertEqual(init_kmp('abacabadabacabacaba')[1], [-1, 0, 1, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3])
        
    def test_fibb8(self):
        self.assertEqual(init_kmp(fibb_str(8))[1], [-1, 0, 0, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 5, 4, 5, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21])

                         
class TestFibbStr(unittest.TestCase):
    def test_fibb8(self):
        self.assertEqual(fibb_str(8), 'abbabbababbabbababbababbabbababbab')
        
if __name__ == '__main__':
    unittest.main()
