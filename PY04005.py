from math import*
import sys 
# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")

class Point: 
    def __init__(self, x:float, y:float): 
        self.x = x 
        self.y = y 
    @staticmethod 
    def distance(p1, p2): 
        dis = sqrt((pow(p1.x - p2.x, 2)) + (pow(p1.y - p2.y, 2)))
        return dis

class Triangle: 
    def __init__(self, p1, p2, p3): 
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3 
    @staticmethod 
    def validation(p1, p2, p3): 
        edge1 = Point.distance(p1, p2) 
        edge2 = Point.distance(p2, p3)
        edge3 = Point.distance(p3, p1)

        if edge1 + edge2 > edge3 and edge1 + edge3 > edge2 and edge2 + edge3 > edge1: return True 
        return False 
    @staticmethod
    def perimeter(triangle):
        edge1 = Point.distance(triangle.p1, triangle.p2) 
        edge2 = Point.distance(triangle.p2, triangle.p3)
        edge3 = Point.distance(triangle.p3, triangle.p1)
        return float(f"{edge1 + edge2 + edge3:.3f}")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t): 
        x1, y1, x2, y2, x3, y3 = map(float, input().split())

        point1 = Point(x1, y1) 
        point2 = Point(x2, y2) 
        point3 = Point(x3, y3)

        triangle = Triangle(point1, point2, point3)

        if not Triangle.validation(point1, point2, point3): print("INVALID")
        else:
            p = Triangle.perimeter(triangle)
            print(p)
        



