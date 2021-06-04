import sys


def solution():
    m, d = map(int, sys.stdin.readline().split())
    thirtyOne = [1, 3, 5, 7, 8, 10, 12]
    twentyEight = [2]
    thirty = [4, 6, 9, 11]
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

    for i in range(1, m):
        if i in thirtyOne:
            d += 31
        elif i in thirty:
            d += 30
        elif i in twentyEight:
            d += 28
    print(days[d % 7])


solution()
