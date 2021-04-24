import sys


def printer(arr):
    count = 0
    for i in arr:
        for j in i:
            if j == 1:
                count += 1
    return count


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        arr.append(list(map(int, sys.stdin.readline().split())))

    board = [[0] * 100 for _ in range(100)]
    return IC, board, arr


def solution():
    IC, board, arr = getInput()
    for i in arr:
        for j in range(i[1], i[1] + 10):
            for k in range(i[0], i[0] + 10):
                board[j][k] = 1
    return printer(board)


print(solution())