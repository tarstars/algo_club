# gathering info
#house = list([5, 7, 8, 6, 8, 9, 8, 4])
house = list(input())
cash = list([]) # payday so far
prev = list([]) # best previous house
luckies = list([]) # house numbers start with 1, NOT 0. We're humans after all

# planning
for pp in range(len(house)):
    if (pp == 0):
        cash.append(house[pp])
        prev.append(0)
    elif (pp == 1):
        cash.append(house[pp])
        prev.append(0)
    elif (pp == 2):
        cash.append(house[pp] + cash[pp-2])
        prev.append(pp-2+1)
    elif (pp > 2) :
        cash.append(house[pp] + max(cash[pp-2], cash[pp-3]))
        prev.append(cash.index(max(cash[pp-2], cash[pp-3])) + 1)
        
#print(prev)
#print(cash)

payday = max(cash[-1], cash[-2])

# execution
luckies.append(cash.index(max(cash[-1], cash[-2]))+1)
while (prev[luckies[-1] - 1] > 0):
    luckies.append(prev[luckies[-1] - 1])
    
luckies.sort()
print(luckies)

# queue the music
print(payday)