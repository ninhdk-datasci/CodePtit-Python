from math import *

def check(s): 
    unique = set(s)
    return len(unique) % 2 == 1  


t = int(input()) 

for _ in range(t): 
    num = int(input())

    res =  []
    for i in range(2, 999+1, 2): 
        res.append(str(i) + str(i)[::-1]) 
    
    for i in res: 
        if int(i) >= num: 
            continue
        if check(i) :print(i, end=' ')
    print()