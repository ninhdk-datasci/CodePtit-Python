lower , upper = 0, 0 

s =  input() 

for c in s: 
    if 'a' <= c <= 'z': lower += 1 
    if 'A' <= c <= 'Z': upper += 1 

if upper > lower: s = s.upper() 
else: s = s.lower() 

print(s) 



