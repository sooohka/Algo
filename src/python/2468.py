import sys


def getInput():
    size = int(sys.stdin.readline())
    arr = []
    for _ in range(size):
        arr.append(list(map(int, sys.stdin.readline().split())))
    # size = 5
    # arr = [[6, 8, 2, 6, 2], [3, 2, 3, 4, 6], [6, 7, 3, 3, 2], [7, 2, 5, 3, 6], [8, 9, 5, 2, 7]]
    return size, arr


def DFS(size, arr, visited, sy, sx):
    stack = [[sy, sx]]
    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited[sy][sx] = True
    while stack:
        cy, cx = stack.pop()
        # print("[",cy, cx,"]",end=' ')
        for i in move:
            my, mx = cy + i[0], cx + i[1]
            if not (my >= 0 and my < size and mx >= 0 and mx < size):
                continue
            if not visited[my][mx]:
                visited[my][mx] = True
                stack.append([my, mx])


def solution():
    size, arr = getInput()
    #비가 안올수도 있음으로 안전지대는 항상 1이상이여야함
    max=1
    #높이가 100까지임으로 즉 비가 100까지 올수있음으로 100까지의 경우 계산    
    for i in range(1, 100):
        count=0
        # size만큼 False로 채워진 2차원 리스트 선언
        visited = [[False for _ in range(size)] for _ in range(size)]
        # 물에 잠기는 거 확인
        for j in range((size)):
            for k in range(size):
                if arr[j][k] <= i:
                    visited[j][k] = True
        # 모든 배열요소를 선언하면서 방문하지 않은 요소에 도착하면 DFS해서 방문한 곳체크하고 Count 1증가
        for j in range(size):
            for k in range(size):
                if visited[j][k]:
                    continue
                DFS(size, arr, visited, j, k)
                count += 1
        if max<count:
            max=count
    print(max) 
solution()