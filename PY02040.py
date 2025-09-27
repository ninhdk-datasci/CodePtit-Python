from math import * 

N = int(input()) 

matrice = [] 

for i in range(N): 
    row = list(map(int, input().split())) 
    matrice.append(row) 

K = int(input())

row = len(matrice) 
col = len(matrice[0]) 

up = 0 
down = 0 

for i in range(row): 
    for j in range(col): 
        if i < (N - j - 1): up += matrice[i][j] 
        elif i > (N - j - 1) : down += matrice[i][j] 

diff = abs(up - down) 


if diff > K:
    print('NO', diff, sep='\n') 
else: 
    print('YES', diff, sep='\n')   

