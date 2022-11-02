n = int(input())

movie_info = {}
for i in range(n):
    name, score, num = input().split()
    movie_info[name] = (int(score), int(num))
sorted_movie_info  = sorted(movie_info.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)
for movie_info in sorted_movie_info:
    print(movie_info[0])    