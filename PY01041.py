from math import * 

t = int(input()) 

for _ in range(t): 

    num = input() 

    i = 0 
    j = 1
    ind = [] 
    check = True
    if len(num) < 3: 
        check = False 
    else:       
        while i < j and j < len(num):
            if num[i] == num[j]: 
                check = False
                break  
            elif num[i] < num[j]:
                if len(ind) > 0: 
                    check = False
                    break
                else: 
                    i += 1 
                    j += 1 
            else: 
                if len(ind) > 0: 
                    i += 1 
                    j += 1 
                else: 
                    ind.append(i) 
                    i += 1 
                    j += 1 
        if len(ind) > 1: check = False 
    if(check): print('YES')
    else: print('NO')

