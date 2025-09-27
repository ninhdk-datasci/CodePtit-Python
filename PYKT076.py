from math import * 
# import sys 

# sys.stdin = open(r"/home/ninhdb/Desktop/CodePtit/inp.txt", 'r') 
# sys.stdout = open(r'/home/ninhdb/Desktop/CodePtit/out.txt', 'w')  


class Genre: 
    genre_dict = {} 

    def __init__(self, order, name): 
        self.code = f'TL{order+1:03d}' 
        self.name = name
        Genre.genre_dict[self.code] = self.name

if __name__ == '__main__':

    N, M = map(int, input().split()) 

    for i in range(N): 
        genre = Genre(i, input()) 

    movies = []

    for i in range(M): 
        code = f'P{i+1:03d}' 
        genre_code = input() 
        date = input() 
        name = input() 
        chap = int(input()) 
        movie = [code, Genre.genre_dict[genre_code], date, name, chap] 
        movies.append(movie) 

    movies.sort(key=lambda m : (m[2], m[3], -m[4])) 

    for m in movies: 
        print(' '.join(map(str, m)))

