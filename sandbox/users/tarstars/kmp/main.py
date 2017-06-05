#!/usr/bin/env python3

import unittest

def fibb_str(n):
    a = 'a'
    b = 'b'
    for _ in range(n):
        a, b = b, a + b
    return a


def init_kmp(pat):
    pos = -1
    f = [pos] * len(pat)
    for ind in range(1, len(pat)):
        while pos >= 0 and pat[pos] != pat[ind]:
            pos = f[pos]
        pos = pos + 1
        f[ind] = pos
    return (str(pat), f)


def apply_kmp(pat, f, s):
    pos = 0
    ans = []
    for ind in range(len(s)):
        while pos >= 0 and pat[pos] != s[ind]:
            pos = f[pos]
        pos = pos + 1
        if pos == len(pat):
            ans.append(ind - len(pat) + 1)
            pos = pos - 1
            while pos >= 0 and pat[pos] != s[ind]:
                pos = f[pos]
    return ans


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


class TestFullKMP(unittest.TestCase):
    def test_short_00(self):
        pat, f = init_kmp('a')
        self.assertEqual(apply_kmp(pat, f, 'bcdef'), [])
        self.assertEqual(apply_kmp(pat, f, 'abcdef'), [0])
        self.assertEqual(apply_kmp(pat, f, 'bacdef'), [1])
        self.assertEqual(apply_kmp(pat, f, 'bcadef'), [2])
        self.assertEqual(apply_kmp(pat, f, 'bcdaef'), [3])
        self.assertEqual(apply_kmp(pat, f, 'bcdeaf'), [4])
        self.assertEqual(apply_kmp(pat, f, 'bcdefa'), [5])

    def test_short_01(self):
        pat, f = init_kmp('a')
        self.assertEqual(apply_kmp(pat, f, 'aabcdef'), [0, 1])
        self.assertEqual(apply_kmp(pat, f, 'abacdef'), [0, 2])
        self.assertEqual(apply_kmp(pat, f, 'abcadef'), [0, 3])
        self.assertEqual(apply_kmp(pat, f, 'abcdaef'), [0, 4])
        self.assertEqual(apply_kmp(pat, f, 'abcdeaf'), [0, 5])
        self.assertEqual(apply_kmp(pat, f, 'abcdefa'), [0, 6])

    def test_word_00(self):
        pat, f = init_kmp('abacaba')
        self.assertEqual(apply_kmp(pat, f, 'qwrefastrtadfas'), [])
        self.assertEqual(apply_kmp(pat, f, 'abacabaqwrefastrtadfas'), [0])
        self.assertEqual(apply_kmp(pat, f, 'abacabaqwrefastrtadfasabacaba'), [0, 22])
        self.assertEqual(apply_kmp(pat, f, 'qwrefaabacabastrtadfas'), [6])
        self.assertEqual(apply_kmp(pat, f, 'qwreabacabafastabacabartadabacabafas'), [4, 15, 26])
        self.assertEqual(apply_kmp(pat, f, 'qwrabacabaabacabaabacabaefastrtadfas'), [3, 4, 17])
        
        
if __name__ == '__main__':
    unittest.main()
