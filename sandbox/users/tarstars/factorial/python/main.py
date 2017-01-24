import sys

n=int(input())

ans = 1
for t in range(1, n+1):
    ans *= t
    
print(ans)
