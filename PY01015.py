import sys

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")



def check(n):
    l = len(n)
    for i in range(l-1):
        if n[i] > n[i+1]: return False;  
    return True

t = int(input())

for _ in range(t): 
    n = input()
    if check(n): print('YES')
    else: print('NO')


