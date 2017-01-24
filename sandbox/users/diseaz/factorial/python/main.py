#!/usr/bin/python3
# -*- coding: utf-8 -*-

import functools

n = int(input())
result = functools.reduce(
    lambda r, i: r * i,
    range(1, n + 1),
    1
)
print (result)
