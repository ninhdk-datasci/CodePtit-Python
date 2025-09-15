import math 
import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

t = int(input())

for _ in range(t):
    
    n = int(input())
    A = list(map(int, input().split()))

    A.sort()

    cnt = 0 

    for i in range(n-2):
        if A[i] >= 0: break; 
        if i > 0 and A[i] == A[i-1] : 
            continue

        left = i + 1 
        right = len(A) - 1 

        while left < right: 
            
            total = A[i] + A[left] + A[right] 

            if total == 0 : 
                cnt += 1
                left += 1 
                while A[left] == A[left - 1] and left < right: 
                    left += 1  
            elif total < 0: left += 1  
            else: right -= 1 

    print(cnt) 
















