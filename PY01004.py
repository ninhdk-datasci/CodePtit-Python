from math import *
def isPrime(n:int) -> bool:
    for i in range(2, int(sqrt(n))+1):
        if n % 2 == 0 : return False 
    return n > 1 

def coPrime(a: int, b:int)->bool: 
    return gcd(a, b) == 1 

if __name__ == '__main__':
    t = int(input()) 
    while t > 0: 
        n = int(input())
        cnt = 0 
        for i in range(1, n):
            if coPrime(n, i): cnt += 1 
        if isPrime(cnt): print('YES') 
        else: print('NO') 
        t -= 1 
