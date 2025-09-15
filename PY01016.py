# import sys

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


t = int(input())

for _ in range(t): 
    s = input()

    res = ""

    for i in range(len(s)): 
        if '1' <= s[i] <= '9': 
            res += (s[i-1] * int(s[i]))

    print(res)



