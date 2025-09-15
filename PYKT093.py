import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 


class Student: 
    all = []

    def __init__(self, name, score1, score2, score3): 
        
        name = name.strip().split()
        name = [x.capitalize() for x in name] 
        name = " ".join(name) 

        self.name = name 
        self.score1 = score1 
        self.score2 = score2 
        self.score3 = score3
        self.avg_score = ((score1*3) + (score2*3) + (score3*2)) / 8
        
        Student.all.append(self)

    def __repr__(self): 
        return f"{self.code} {self.name} {self.avg_score + 1e-8:.2f} {self.rank}" 

if __name__ == "__main__": 
    n = int(input()) 

    for i in range(n): 
        name = input() 
        score1 = float(input())
        score2 = float(input()) 
        score3 = float(input()) 

        stu = Student(name, score1, score2, score3) 
        stu.code = f"SV{i+1:02d}" 

    
    Student.all.sort(key=lambda s: (-s.avg_score, s.code))

    count = 0 
    rank = 0 
    prev_score = None 

    for st in Student.all: 
        count += 1 

        if prev_score is None or st.avg_score < prev_score: 
            rank = count 

        st.rank = rank 
        prev_score = st.avg_score

    for st in Student.all: 
        print(st)


    
