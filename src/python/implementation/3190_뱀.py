# 뱀의 머리가 몸통에 닿거나 벽에 닿을때까지 방향전환안하면 게임종료
import sys
from collections import deque

# 현재 바라보고 있는 방향
# 북 동 남 서
dir = 1


def getInput():
    N = int(sys.stdin.readline())
    K = int(sys.stdin.readline())
    apples = []
    for _ in range(K):
        # 행 열 순으로 입력받음
        apples.append(list(map(int, sys.stdin.readline().split())))
    L = int(sys.stdin.readline())
    moves = []
    for _ in range(L):
        a, b = sys.stdin.readline().split()
        moves.append([int(a), b])
    board = [[False] * N for _ in range(N)]
    for i in range(len(apples)):
        board[apples[i][0] - 1][apples[i][1] - 1] = 1
    return board, moves


def printer(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()


def rotate(D):
    # 북 동 남 서
    global dir
    # 왼
    if D == "L":
        dir = (dir + 4 - 1) % 4
    # 오
    elif D == "D":
        dir = (dir + 4 + 1) % 4
    else:
        print("방향 이상")
    return dir


def check(board, ly, lx):
    # ly lx 현재 오려고하는 위치
    # 벽에 부딪히면 종료
    if ly >= len(board) or ly < 0:
        return False
    if lx >= len(board) or lx < 0:
        return False
    if board[ly][lx] == 1:
        return True
    # 자기자신과 부딪히면 종료
    if board[ly][lx] == "T":
        return False
    return True


def solution():
    board, moves = getInput()
    count = 0
    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    snake = deque()
    snake.append([0, 0])
    cy = snake[len(snake) - 1][0]
    cx = snake[len(snake) - 1][1]
    board[cy][cx] = "T"
    flag = 0
    # 뱀이 있는곳  True
    while True:
        cy = cy + dy[dir]
        cx = cx + dx[dir]
        snake.append([cy, cx])
        count += 1
        # 못가는 상황이면
        if not check(board, cy, cx):
            return count
        # 간 타일에 사과가없다면
        if not board[cy][cx] == 1:
            y, x = snake.popleft()
            board[y][x] = False
        board[cy][cx] = "T"
        # 다돌고 방향전환
        if flag < len(moves) and count == moves[flag][0]:
            rotate(moves[flag][1])
            flag += 1


print(solution())
