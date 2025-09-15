import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

t = int(input()) 

for _ in range(t): 
    n = int(input()) 

    A = list(map(int, input().split())) 
    B = list(map(int, input().split())) 

    A.sort() 
    B.sort() 

    match = all(a <= b for a, b in zip(A,B)) 

    print("YES" if match else "NO") 