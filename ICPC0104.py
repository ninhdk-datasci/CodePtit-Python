t = int(input())

for i in range(t):
    string = input()
    
    string += 'n'
    num = "" 
    res = 1e9 

    for ch in string: 
        if ch.isdigit(): 
            num += ch 
        else: 
            if num != "":
                res = min(res, int(num)) 
                num = ""
    
    print(res) 

