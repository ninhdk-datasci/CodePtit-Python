from math import * 

def GCD(a, b): 
    if b == 0: return a
    return GCD(b, a%b)


def isPrime(n):
    for i in range(2, int(sqrt(n)) + 1): 
        if n % i == 0: return False
    return  n > 1 

def total(n): 
    sum = 0 
    while n != 0: 
        m = n % 10 
        sum += m 
        n = n // 10 
    return sum 


t  = int(input())

for _ in range(t): 
    a, b = map(int, input().split())

    gcd = GCD(a,b)

    res = total(gcd)

    if isPrime(res): print('YES')
    else: print('NO')