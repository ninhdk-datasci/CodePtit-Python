import math 
import sys 
# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

# def add_strings(a, b):
#     a, b = a.zfill(max(len(a), len(b))), b.zfill(max(len(a), len(b)))
#     carry = 0 
#     result = []
#     for i in range(len(a)-1, -1, -1):
#         total = int(a[i]) + int(b[i]) + carry 
#         carry = total // 10 
#         result.append(str(total%10))
#     if carry: result.append(str(carry)) 
#     return "".join(result[::-1]).lstrip('0') or '0'


def minSum(X1, X2, p, q): 
    cmin = str(min(p, q))
    X1_new = X1.replace(str(p), cmin).replace(str(q), cmin)
    X2_new = X2.replace(str(p), cmin).replace(str(q), cmin)
    return int(X1_new) + int(X2_new)

def maxSum(X1, X2, p, q): 
    cmax = str(max(p, q))
    X1_new = X1.replace(str(p), cmax).replace(str(q), cmax)
    X2_new = X2.replace(str(p), cmax).replace(str(q), cmax)
    return int(X1_new) + int(X2_new)

if __name__ == '__main__':
    t = int(input()) 
    for _ in range(t):
        p, q = map(int, input().split())
        X1 = input()
        if len(X1.split()) > 1 : X1, X2 = X1.split()
        else: X2 = input()
        print(minSum(X1, X2, p, q), maxSum(X1, X2, p, q))



















