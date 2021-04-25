import sys


def getInput():
    N, L, R = map(int,sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    return L, R, board


def solution():
    L, R, board = getInput()
    print(L, R, board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            
    return


solution()