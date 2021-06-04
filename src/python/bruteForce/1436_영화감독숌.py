import sys


def getInput():
    N = int(sys.stdin.readline())
    return N


def solution():
    N = getInput()
    movies = [False]
    six = 666
    while len(movies) != 10001:
        if "666" in str(six):
            movies.append(six)
        six += 1

    return movies[N]


print(solution())