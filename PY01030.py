from math import * 

arr = []

def GCD(n, k):
    global arr 
    for i in range(10, 100001): 
        if gcd(i, n) == 1 and len(str(i)) == k: 
            arr.append(i)


N, K = map(int , input().split())
 
GCD(N, K) 


for i in range(0 , len(arr), 10): 
    group = arr[i:i+10] 
    print(" ".join(map(str, group)))




















