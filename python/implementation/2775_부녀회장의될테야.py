import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        k = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        arr.append([k, n])
    return IC, arr


def solution():
    IC, arr = getInput()
    house = [[0] * 15 for _ in range(15)]
    for i in range(15):
        house[0][i] = i
    for i in range(1, 15):
        for j in range(1, 15):
            total = 0
            for k in range(1, j + 1):
                total += house[i - 1][k]
            house[i][j] = total
    for i in range(IC):
        print(house[arr[i][0]][arr[i][1]])


solution()
