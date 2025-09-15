# import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


t = int(input()) 

for _ in range(t): 

    n = input() 
    check = True 

    for c in n: 
        if c != '4' and c != '7': 
            check = False 
            break

    if check: print("YES") 
    else: print("NO") 