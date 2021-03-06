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


# 0λΆ 1λ 2λ¨ 3μ
def solution():
    global count
    # λΆ λ λ¨ μ
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cy, cx, board = getInput()
    while True:
        # νμ¬ μμΉ μ²­μ
        if board[cy][cx] == 0:
            board[cy][cx] = 2
            count += 1
        # νμ
        else:
            # 3λ² λͺ¨λ  λ°©ν₯μ μ²­μν κ³³μ΄ μμΌλ©΄
            if (
                board[cy + dy[0]][cx + dx[0]] != 0
                and board[cy + dy[1]][cx + dx[1]] != 0
                and board[cy + dy[2]][cx + dx[2]] != 0
                and board[cy + dy[3]][cx + dx[3]] != 0
            ):
                #λ°λ‘ λ€μ λ¨Ήμλ νμ μ΄ μμΌλ©΄ μ¦ μμμ μμ§λ§ κΈΈμ΄ μμλ λ€λ‘ μ΄λ
                if board[cy + dy[(dir + 2) % 4]][cx + dx[(dir + 2) % 4]] == 2:
                    cy += dy[(dir + 2) % 4]
                    cx += dx[(dir + 2) % 4]
                #μλλ©΄ μ’λ£
                else:
                    break
            # 1λ² μΌμͺ½μ λ¨Ήμκ² μμΌλ©΄
            elif board[cy + dy[(dir + 3) % 4]][cx + dx[(dir + 3) % 4]] == 0:
                rotate()                
                cy += dy[(dir) % 4]
                cx += dx[(dir) % 4]
            # 2λ² μΌμͺ½μ λ¨Ήμκ² μλ€λ©΄
            elif board[cy + dy[(dir + 3) % 4]][cx + dx[(dir + 3) % 4]] != 0:
                rotate()

    return count


print(solution())