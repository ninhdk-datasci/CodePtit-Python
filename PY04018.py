import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

priority_score = {
    '1':2.0, 
    '2':1.5,
    '3':1.0,
    '4':0.0 
}

subject = {
    'A':'TOAN',
    'B':'LY',
    'C':'HOA'
}

class Teacher: 
    teachers = []
    def __init__(self, i, name, addmission_code, IT_score, expertise_score): 
        self.GV_code = f"GV{i+1:02d}" 
        self.name = name
        self.subj = subject[addmission_code[0]] 
        score = IT_score*2 + expertise_score + priority_score[addmission_code[1]] 
        self.score = float(round(score, 1))
        self.result = "TRUNG TUYEN" 
        if self.score < 18.0: self.result = "LOAI"   
        Teacher.teachers.append(self) 
    
    def __repr__(self): 
        return f"{self.GV_code} {self.name} {self.subj} {self.score} {self.result}"

if __name__ == "__main__": 
    n = int(input()) 

    for i in range(n): 
        name = input() 
        addmission_code = input() 
        IT_score = float(input())
        expertise_score = float(input()) 
        t = Teacher(i, name, addmission_code, IT_score, expertise_score)

    Teacher.teachers.sort(key = lambda t: (-t.score)) 

    for teacher in Teacher.teachers: 
        print(teacher) 






