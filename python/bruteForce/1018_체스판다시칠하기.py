import sys


def getInputs():
    col, row = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(col):
        board.append([i for i in sys.stdin.readline()])
    return col, row, board


def getMin(sy, sx, board, min):
    for start in ["B", "W"]:
        temp = 0
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0 and board[sy + i][sx + j] != start:
                        temp += 1
                    elif j % 2 == 1 and board[sy + i][sx + j] == start:
                        temp += 1

                elif i % 2 == 1:
                    if j % 2 == 0 and board[sy + i][sx + j] == start:
                        temp += 1
                    elif j % 2 == 1 and board[sy + i][sx + j] != start:
                        temp += 1
        if min > temp:
            min = temp
    return min


def solution():
    col, row, board = getInputs()
    min = 64
    for i in range(col - 7):
        for j in range(row - 7):
            min = getMin(i, j, board, min)
    return min


print(solution())
