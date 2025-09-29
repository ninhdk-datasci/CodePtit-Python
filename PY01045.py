from math import * 

s = input().strip() 
n = len(s)
rs = s[::-1] 
prev = [0]*(n+1)
cur = [0]*(n+1)

for i in range(1, n+1): 
    for j in range(1, n+1): 
        if(s[i-1] == rs[j-1]): 
            cur[j] = prev[j-1] + 1 
        else:
            cur[j] = max(cur[j-1], prev[j])  
    prev, cur = cur, prev 
print(n - prev[n])