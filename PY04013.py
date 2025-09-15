from collections import defaultdict 

import sys 

sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")


class Station:
    map = defaultdict(float) 
    def __init__(self, name, start, end, rainfall): 
        self.name = name 
        self.start = start
        self.end = end 
        self.rainfall = rainfall 

        convert_start = Station.convert(self.start) 
        convert_end = Station.convert(self.end)

        total_rainfall = self.rainfall / ((convert_end - convert_start))

        Station.map[self.name] += total_rainfall

    @staticmethod
    def convert(time):
        detach = time.split(':')
        total = float(detach[0])*60 + float(detach[1])
        return total 
    


x = int(input())

for _ in range(x):
    name = input()
    start = input()
    end = input()
    rainfall = float(input())
    station = Station(name, start, end, rainfall)

list = []

for item in Station.map:
    list.append([item, Station.map[item]])

print(list)


