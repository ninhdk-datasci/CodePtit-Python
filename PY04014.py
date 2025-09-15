# import sys 

# sys.stdin = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\inp.txt", "r")
# sys.stdout = open(r"C:\Users\NinhDB\.vscode\Data\Code Ptit\out.txt", "w")   


class SinhVien:
    def __init__ (self, i, ten, dtb, xl):
        self.ma = 'HS' + f"{i+1:02d}"
        self.ten = ten 
        self.dtb = dtb 
        self.xl = xl 

    def __repr__(self): 
        return f"{self.ma} {self.ten} {round(self.dtb + 1e-3, 1)} {self.xl}"

n = int(input())
lst = []


for i in range(n):
    ten = input() 
    diem = list(map(float, input().split()))

    tong = sum(diem) 
    tong += (diem[0] + diem[1])

    dtb = tong/12
    xl = ""

    if dtb >= 9: xl = 'XUAT SAC'
    elif 8 <= dtb <= 8.9: xl = 'GIOI'
    elif 7 <= dtb <= 7.9: xl = 'KHA'
    elif 5 <= dtb <= 6.9: xl = 'TB'
    else: xl = 'YEU'

    sv = SinhVien(i, ten, dtb, xl)
    lst.append(sv)

lst.sort(key=lambda s: (-s.dtb, s.ma))
for s in lst: 
    print(s)