from math import*
import sys 
# sys.stdin = open(r'C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt', 'r') 
# sys.stdout = open(r'C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt', 'w') 

def convert(s:str)->str:
    map = {
        10:'A', 
        11:'B', 
        12:'C', 
        13:'D', 
        14:'E', 
        15:'F'  
    }
    total = 0  
    s = s[::-1]
    for i in range(len(s)):
        if s[i] == '1': 
            total += int(pow(2, i))
    if total >= 10 and total <= 15: return map[total]
    return str(total)

T = int(input())

for _ in range(T):

    b = int(input())
    bin_str = input()

    par = int(log2(b))
    while len(bin_str) % par != 0: 
        bin_str = '0' + bin_str 

    res = "" 
    for i in range(0, len(bin_str) - par + 1, par):
        s = bin_str[i:i+par]
        res += convert(s)

    print(res) 
