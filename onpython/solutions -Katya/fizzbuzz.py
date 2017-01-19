x=list(range(1,16))
for t in x:
    if t%3==0 and t%5==0:
        print('Fizzbuzz')
        continue
    if t%3==0:
        print('Buzz')
    if t%5==0:
        print('Fizz')
    else:
        print(t)
