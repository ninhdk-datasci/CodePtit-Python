from math import * 

mark = [False] * 30000 

n = int(input()) 

arr = list(map(int, input().split())) 

for x in arr: mark[x] = True 

res = n + 1
for i in range(1, n+1):
    if not mark[i]: 
        res = i 
        break
print(res)   

