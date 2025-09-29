
coefs = {
    'A': [10, 12, 14, 20], 
    'B': [10, 11, 13, 16], 
    'C': [9,  10, 12, 14], 
    'D': [8, 9, 11, 13] 
}


depart = int(input())

departs = {}
for _ in range(depart): 

    code, name = input().split(" ", 1) 

    departs[code] = name 

emp = int(input()) 

for _ in range(emp): 
    emp_code = input() 
    emp_name = input()
    salary = int(input()) 
    workdays = int(input()) 
    group = emp_code[0:1] 
    exper = int(emp_code[1:3])
    de_code = emp_code[3:]

    if 1 <= exper <= 3: salary = salary * coefs[group][0] * workdays * 1000
    elif 4 <= exper <= 8: salary = salary * coefs[group][1] * workdays * 1000
    elif 9 <= exper <= 15: salary = salary * coefs[group][2] * workdays * 1000
    elif  exper > 16 : salary = salary * coefs[group][3] * workdays * 1000
    print(emp_code, emp_name, departs[de_code], salary, sep = " ") 




















