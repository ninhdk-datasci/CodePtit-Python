import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

class Team: 
    map = {}
    def __init__(self, i, team_name, university): 
        self.team_code = f"Team{i+1:02d}" 
        self.team_name = team_name 
        self.university = university
        Team.map[self.team_code] = [self.team_name, self.university] 


if __name__ == "__main__": 
    n = int(input()) 

    for i in range(n): 
        team_name = input() 
        university = input() 
        group = Team(i, team_name, university) 

    m = int(input()) 

    contestants = []

    for i in range(m):
        contest_code = f"C{i+1:03d}"  
        name = input() 
        team_code = input() 
        contestant = [contest_code, name, Team.map[team_code][0],  Team.map[team_code][1]]
        contestants.append(contestant)
    contestants.sort(key = lambda t: (t[1])) 

    for t in contestants: 
        print(" ".join(t))  







































