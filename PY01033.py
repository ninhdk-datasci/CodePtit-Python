from math import *

L, R = map(int , input().split()) 

coprime = [[False]*(R+1) for _ in range(R+1)] 

for i in range(L, R+1): 
    for j in range(L, R+1): 
        coprime[i][j] = (gcd(i, j) == 1) 


for a in range(L, R-1): 
    for b in range(a+1, R): 
        if not coprime[a][b]: 
            continue
        for c in range(b+1, R+1): 
            if coprime[b][c] and coprime[a][c]: 
                print(f'({a}, {b}, {c})')



    