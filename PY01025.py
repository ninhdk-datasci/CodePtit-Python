# import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


N = input() 
while len(N) % 3 != 0: 
    N = '0' + N 

l = len(N) 
substr = []

for i in range(l-1, -1, -3): 
    sub = N[i-2:i+1]
    substr.append(sub)
substr = substr[::-1]
substr[0] = str(int(substr[0]))
print(",".join(substr))


'''
053920529
012345678
'''