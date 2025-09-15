import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


arr = list(map(int, sys.stdin.read().split())) 

res = set() 

res.update([x % 42 for x in arr]) 

print(len(res))  