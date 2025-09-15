import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r") 
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w") 

class Contestant:
    contestants = []
    def __init__(self, i, name, theoretical_score, practical_score): 
        if len(theoretical_score) > 1 and '.' not in theoretical_score: 
            theoretical_score = theoretical_score[:-1] + "." + theoretical_score[-1] 
        if len(practical_score) > 1 and '.' not in practical_score: 
            practical_score = practical_score[:-1] + "." + practical_score[-1] 
        self.code = f"TS{i+1:02d}" 
        self. name = name 
        self.score = round((float(theoretical_score) + float(practical_score)) / 2, 2) 
        self.result = "TRUOT"
        if 5 <= self.score < 8: self.result = "CAN NHAC" 
        elif 8 <= self.score <= 9.5: self.result = 'DAT' 
        elif self.score > 9.5: self.result = "XUAT SAC" 
        Contestant.contestants.append(self) 

    def __repr__(self): 
        return f"{self.code} {self.name} {self.score:.2f} {self.result}" 

if __name__ == "__main__": 
    n = int(input()) 

    for i in range(n): 
        name = input() 
        theoretical_score = input()
        practical_score = input() 
        contestant = Contestant(i, name, theoretical_score, practical_score) 

    Contestant.contestants.sort(key = lambda c: (-c.score)) 

    for cont in Contestant.contestants: 
        print(cont) 

    


