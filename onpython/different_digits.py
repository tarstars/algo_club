#!/bin/python

import random

def find_different(x):
    l = 0
    r = len(x)-1
    while l != r - 1:
        m = (l + r) // 2
        if x[m] == 0:
            l = m
        else:
            r = m
    return l,r
   
x=[random.randint(0,1) for t in range(10)]
x[0] = 0
x[-1] = 1
print(find_different(x))
