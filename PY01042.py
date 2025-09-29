from math import * 

t = int(input())

for _ in range(t): 
    s = input() 

    check = True
    for c in s: 
        if c != '1' and c != '2' and c != '0': 
            check = False 
            break

    if check: print('YES') 
    else: print('NO')
