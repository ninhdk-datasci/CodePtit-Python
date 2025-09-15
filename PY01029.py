from math import * 


def GCD(a, b): 
    if b == 0: return a 
    return GCD(b, a%b) 


t = int(input()) 

for _ in range(t): 
    a = input().strip()
    b = a[::-1]
    if GCD(int(a), int(b)) == 1: print('YES')
    else: print('NO')
    # print(GCD(int(a), int(b)))

