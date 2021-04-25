import sys

dir = 0
count = 0


def getInput():
    global dir
    N, M = map(int, sys.stdin.readline().split())
    cy, cx, dir = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    return cy, cx, board


def rotate():
    global dir
    if dir == 0:
        dir = 3
    else:
        dir -= 1


# 0북 1동 2남 3서
def solution():
    global count
    # 북 동 남 서
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cy, cx, board = getInput()
    while True:
        # 현재 위치 청소
        if board[cy][cx] == 0:
            board[cy][cx] = 2
            count += 1
        # 탐색
        else:
            # 3번 모든 방향에 청소할곳이 없으면
            if (
                board[cy + dy[0]][cx + dx[0]] != 0
                and board[cy + dy[1]][cx + dx[1]] != 0
                and board[cy + dy[2]][cx + dx[2]] != 0
                and board[cy + dy[3]][cx + dx[3]] != 0
            ):
                #바로 뒤에 먹었던 흔적이 있으면 즉 음식은 없지만 길이 있을때 뒤로 이동
                if board[cy + dy[(dir + 2) % 4]][cx + dx[(dir + 2) % 4]] == 2:
                    cy += dy[(dir + 2) % 4]
                    cx += dx[(dir + 2) % 4]
                #아니면 종료
                else:
                    break
            # 1번 왼쪽에 먹을게 있으면
            elif board[cy + dy[(dir + 3) % 4]][cx + dx[(dir + 3) % 4]] == 0:
                rotate()                
                cy += dy[(dir) % 4]
                cx += dx[(dir) % 4]
            # 2번 왼쪽에 먹을게 없다면
            elif board[cy + dy[(dir + 3) % 4]][cx + dx[(dir + 3) % 4]] != 0:
                rotate()

    return count


print(solution())