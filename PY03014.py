

t = int(input()) 

for _ in range(t): 
    
    expr = input() 

    par = ""

    for p in expr: 
        if p == '(' or p == ')': par += p 

    hashmap = []
    stack = [] 
    for i in range(len(par)): 
        if par[i] == '(':
            stack.append(i) 
        else: 
            top = stack.pop() 
            hashmap.append([top, i])  

    res = [0] * (len(par))
    hashmap.sort() 

    for i in range(len(hashmap)): 
        pair = hashmap[i] 
        res[pair[0]] = res[pair[1]] = i + 1 

    print(' '.join(map(str, res))) 













