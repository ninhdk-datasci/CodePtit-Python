def fac(s):
    num = int(s) 

    res = 1 
    for i in range(1, num+1): 
        res = res*i 

    return res 

if __name__ == "__main__": 
    t = int(input())

    for _ in range(t): 
        n = input() 

        total = 0 
        for c in n: 
            total += fac(c) 

        if total == int(n) : print("Yes")
        else: print("No")



