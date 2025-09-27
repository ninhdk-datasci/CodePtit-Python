from math import * 

t = int(input()) 

for _ in range(t): 

    num = input().strip()

    if len(num) > 1: 
        check = num[-2:]
        if check == '86': print('YES')
        else: print('NO')
    else: print('NO')


    

















