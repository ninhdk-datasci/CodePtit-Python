import sys 
from math import*


# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 

def sieve(n): 
    primes = [True]*(1000005) 
    primes[0] = primes[1] = False 

    for i in range(2, int(sqrt(1000000)) + 1): 
        if primes[i]: 
            for j in range(i*i, 1000001, i): 
                primes[j] = False 

    arr = [] 

    for i in range(1000001): 
        if len(arr) == n: 
            break
        if primes[i]: 
            arr.append(i) 

    return arr 


if __name__ == "__main__": 

    N, X = map(int, input().split()) 

    arr = sieve(N) 
    res = [X] 

    i = 0 
    while i < len(arr): 
        res.append(res[-1] + arr[i]) 
        i += 1 

    print(" ".join(map(str, res)))  





