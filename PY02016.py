from collections import defaultdict 

t = int(input()) 

for _ in range(t): 
    n = int(input()) 
    arr = list(map(int, input().split())) 

    hashmap = defaultdict(int) 

    for x in arr: hashmap[x] += 1 

    max_value = n/2 
    k = 0 
    for key in hashmap.keys():
        if hashmap[key] > max_value: 
            max_value = hashmap[key] 
            k = key  

    if k == 0: print('NO') 
    else: print(k)
