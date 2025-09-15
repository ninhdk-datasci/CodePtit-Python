import sys 
from collections import defaultdict 


# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    hash = defaultdict(int) 
    for _ in range(n): 
        num = int(input()) 
        hash[num] += 1 

    fre = max(hash.values()) 

    res = min([x for x in hash.keys() if hash[x] == fre]) 

    print(res) 