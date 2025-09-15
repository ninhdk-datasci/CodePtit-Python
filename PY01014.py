

a, K, N = map(int, input().split())

i = K - (a % K)

N -= a

b = [x for x in range(i, N + 1, K)]

if len(b) == 0: print(-1)
else: 
    b = [str(i) for i in b]
    print(" ".join(b))









