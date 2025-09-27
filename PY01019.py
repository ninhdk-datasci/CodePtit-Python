from math import * 

def check(s:str): 
    rev_s = s[::-1] 

    length = len(s) 

    for i in range(1, length): 
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(rev_s[i]) - ord(rev_s[i-1])): return False  

    return True 


t = int(input()) 

for _ in range(t): 
    s = input().strip() 

    if check(s): print('YES') 
    else: print('NO') 
