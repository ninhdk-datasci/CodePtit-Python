from math import *
# import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")



def check(num):
    l = len(num)

    sum = 0 
    for i in range(l-1):
        x = int(num[i]) 
        sum += x 
        if abs(int(num[i]) - int(num[i+1])) != 2:
            return False
    sum += int(num[l-1])
    return sum % 10 == 0

t = int(input())

for _ in range(t):

    num = input()
    if check(num): print('YES')
    else: print('NO')



