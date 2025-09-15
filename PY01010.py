t = int(input()) 

for _ in range(t):
    num = input() 

    if (num[0] == num[-2]) and (num[1] == num[-1]): print('YES')
    else: print('NO')