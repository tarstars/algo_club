# -*- coding: utf-8 -*-
import sys

from add_two_numbers import Solution

if __name__ == '__main__':
    a = input()
    b = input()
    S = Solution()
    sys.stdout.write(str(S.addTwoNumbersFromStdin(a, b)))
