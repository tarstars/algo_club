def next_permutation(a):
  a = list(a)
  n = len(a)
  for q in range(n-2, -1, -1):
    if a[q] < a[q+1]:
      break
  if q > -1:
    for p in range(n - 1, q, -1):
      if a[p] > a[q]:
        break
    a[p], a[q] = a[q], a[p]

  a[q+1:]=sorted(a[q+1:])
  return a

def main():
  print(' '.join(str(t) for t in next_permutation(int(t) for t in input().split())))

if __name__ == '__main__':
  main()
  
  
