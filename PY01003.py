import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


t = int(input()) 

for _ in range(t): 
    n = input() 
    n = list(map(int, n)) 
    
    l = len(n)

    if l > 1: 

        for i in range(l-1, 0, -1): 
            if n[i] >= 5: 
                n[i] = 0 
                n[i-1] += 1 
            else: 
                n[i] = 0 

    for i in n: print(i, end="")
    print()























