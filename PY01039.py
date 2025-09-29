from math import * 

t = int(input()) 

for _ in range(t):
    num = input() 

    n = len(num) 
    i = 0 
    j = 1

    check = True 
    if num[i] != num[j] :
        for a in range(2, n, 2): 
            if num[i] != num[a]: 
                check = False 
                break
        for b in range(3, n, 2): 
            if num[j] != num[b]: 
                check = False
                break
    else: check = False 

    if check: print('YES')
    else: print('NO') 
