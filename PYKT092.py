import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


class Student: 
    student_list = []

    def __init__(self, name, score:float, ethnic, area): 
        self.name = name 
        self.score = score 
        self.ethnic = ethnic 
        self.area = area 
        Student.student_list.append(self) 
    
    def total_score(self): 
        total = self.score 
        if self.area == "1": total += 1.5
        if self.area == "2": total += 1 
        if self.area == "3": total += 0 
        if self.ethnic != "Kinh": total += 1.5 
        return total   

    @staticmethod 
    def fix_name(name): 
        name = name.strip() 
        detach = name.split() 
        detach = [i.capitalize() for i in detach]
        return " ".join(detach) 
    

if __name__ == "__main__":
    n = int(input()) 

    for i in range(n): 
        name = input() 
        score = float(input()) 
        ethnic = input() 
        area = input() 
        student = Student(name, score, ethnic, area) 
        student.name = Student.fix_name(student.name)
        student.score = student.total_score() 
        student.code = f"TS{i+1:02d}" 
        if student.score >= 20.5: student.result = "Do"
        else: student.result = "Truot" 

    Student.student_list.sort(key = lambda s: (-s.score, s.code))

    for s in Student.student_list: 
        print(s.code, s.name, s.score, s.result) 

    
    
    

    
    
        