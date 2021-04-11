import sys
from collections import deque


def solution():
    move = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    IC = int(sys.stdin.readline())
    for _ in range(IC):
        row = int(sys.stdin.readline())
        arr = [[0 for _ in range(row)] for _ in range(row)]
        sy, sx = list(map(int, sys.stdin.readline().split()))
        dy, dx = list(map(int, sys.stdin.readline().split()))
        queue = deque()
        queue.append((sy, sx))
        while queue:
            cy, cx = queue.popleft()
            # 종료조건
            if dx == cx and dy == cy:
                print(arr[dy][dx])
                break
            #  8방향 이동
            for i in range(8):
                my = cy + move[i][0]
                mx = cx + move[i][1]
                if not (0 <= my and 0 <= mx and my < row and mx < row):
                    continue
                if arr[my][mx]:
                    continue
                arr[my][mx] = arr[cy][cx] + 1
                queue.append((my, mx))


solution()