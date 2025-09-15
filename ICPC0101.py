N = int(input())
A = list(map(int, input().split())) 

stack = []

for num in A: 
    if stack and (stack[-1] + num) % 2 == 0: 
        stack.pop() 
    else: stack.append(num) 

print(len(stack))
