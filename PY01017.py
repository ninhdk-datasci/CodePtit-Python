from math import * 

t = int(input()) 

for _ in range(t): 
    
    s = input() 

    left = right = 0 

    hash = [] 
    s = s + " "

    while left <= right and right < len(s): 
        # if right >= len(s): hash.append([s[left], right - left])
        if s[left] == s[right]: right += 1 
        else: 
            hash.append([s[left], right - left])
            left = right 

    for pair in hash: 
        print(''.join(map(str, pair[::-1])), end='')
    
    print()