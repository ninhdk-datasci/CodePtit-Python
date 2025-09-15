import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


class Subject: 
    list_subject = {}

    def __init__(self, code, name): 
        self.code = code
        self.name = name 
        Subject.list_subject[self.code] = self.name 

if __name__ == '__main__': 
    N, M = map(int, input().split())

    for _ in range(N): 
        code = input()
        name = input()

        subject = Subject(code, name)

    timetable = []

    prev = {}

    for i in range(M):
        string = input()
        shift = f"T{i+1:03d} " + string 

        detach = shift.split()
        date = detach[2].split('/')

        tup_date = tuple(date[::-1])
        prev[tup_date] = detach[2]
        detach[2] = tup_date 

        # time = detach[3].split(':')
        # total = int(time[0]) + int(time[1])
        # prev[total] = detach[3]
        # detach[3] = total 

        timetable.append(detach)



    sorted_timetable = sorted(timetable, key=lambda x : (x[2], x[3], x[1])) 

    for shift in sorted_timetable: 
        print(shift[0], shift[1], Subject.list_subject[shift[1]], prev[shift[2]], shift[3], shift[4])

    