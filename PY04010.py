import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


class Contestant:
    def __init__(self, name, date, grade1, grade2, grade3):
        self.name = name 
        self.date = date 
        self.grade1 = grade1 
        self.grade2 = grade2 
        self.grade3 = grade3


name = input()
date = input()
grade1 = float(input())
grade2 = float(input()) 
grade3 = float(input()) 

contestant = Contestant(name, date, grade1, grade2, grade3)

total = contestant.grade1 + contestant.grade2 + contestant.grade3

print(contestant.name, contestant.date, f"{total:.1f}")
