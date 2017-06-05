#!/usr/bin/env python3

import kmp_lib

pat = input()
s = input()

p, f = kmp_lib.init_kmp(pat)
ans = kmp_lib.apply_kmp(p, f, s)

if not ans:
    print("None")
else:
    print(" ".join(str(t) for t in ans))
