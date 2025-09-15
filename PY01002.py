import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


exp = input() 

exp = exp.replace("=", "+")

exp = exp.split("+")

if int(exp[0]) + int(exp[1]) == int(exp[2]): print("YES")
else: print("NO") 
