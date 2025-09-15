from collections import defaultdict 
from math import * 


def primeFac(n): 
    map = defaultdict(int) 

    for i in range(2, int(sqrt(n)) + 1): 
        while n % i == 0: 
            map[i] += 1
            n = n//i 

    if n != 1: map[n] = 1 
    
    res = "1" 

    for key in map.keys(): 
        res = res + " * " + f"{key}^{map[key]}"

    return res


t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    print(primeFac(n)) 


    