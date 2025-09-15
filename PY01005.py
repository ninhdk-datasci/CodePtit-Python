from collections import defaultdict 
# import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 

n = input() 

hash = defaultdict(int) 

for c in n: 
    hash[c] += 1 

check = hash['4'] + hash['7'] 

if check == 4 or check == 7: print("YES") 
else: print("NO") 


