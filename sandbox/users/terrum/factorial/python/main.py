input = int(input())
output = 1;

#a = list(range(input+1))
#b = list(range(1, input+1))

#print(a)
#print(b)

for t in range(1,input+1):
    print(t);
    output *= t;
print(output)