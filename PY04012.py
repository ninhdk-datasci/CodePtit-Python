from collections import defaultdict 
import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


class Student:

    def __init__(self, code, name, _class): 
        self.code = code 
        self.name = name 
        self._class = _class 


    @staticmethod 
    def calculate_grade(s):
        map = defaultdict(int)

        for c in s: 
            map[c] += 1 

        res = 10 

        for c in map.keys(): 
            if c == 'm': res -= map[c]
            if c == 'v': res -= (map[c] * 2)
        return res


if __name__ == "__main__": 
    
    n = int(input())
    list_student = []

    for _ in range(n): 

        code = input()
        name = input()
        _class = input()

        student = Student(code, name, _class)

        list_student.append(student)

    score = {}

    for _ in range(n):
        code, string = input().split()

        score[code] = Student.calculate_grade(string)

    for student in list_student: 

        if int(score[student.code]) <= 0 : 
            print(student.code, student.name, student._class, 0, "KDDK")

        else: 
            print(student.code, student.name, student._class, score[student.code])


    