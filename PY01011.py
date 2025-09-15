def check(s): 
    for c in s: 
        if int(c) % 2 != 0: return False
    unique = set(list(s)) 
    return len(unique) % 2 == 1  and s == s[::-1]


t = int(input()) 

for _ in range(t): 
    num = input() 

    print(check(num))