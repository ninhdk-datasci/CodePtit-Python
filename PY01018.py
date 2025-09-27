from math import * 

P = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

while True: 
    enter = input().split() 

    if enter[0] == '0': break 

    K = int(enter[0]) 

    S = enter[1] 

    res = ''

    for c in S: 
        res = res + P[(P.index(c) + K) % 28] 

    print(res[::-1]) 
