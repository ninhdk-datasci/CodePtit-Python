from math import*
import sys 

sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


t = int(input()) 

for _ in range(t): 
    N, X, M = map(float, input().split())

    res = log(M/N, 1 + X/100) 
    print(ceil(res))