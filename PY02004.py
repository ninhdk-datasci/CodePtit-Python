import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


n = int(input()) 

arr = list(map(int, input().split())) 

res = 0 

for i in range(n-1): 
    if arr[i] != arr[i+1]: 
        res += 1 

print(res) 