from math import*
def isPrime(n:int)->bool:
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0: return False 
    return n > 1 


if __name__ == '__main__':

    N, M = map(int, input().split()) 

    matrix = [] 

    for _ in range(N): 
        row = list(input().split())
        
        row = ['1' if isPrime(int(num)) else '0' for num in row]

        matrix.append(row) 

    for i in range(N): 
        print(' '.join(matrix[i]))