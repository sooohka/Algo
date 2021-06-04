import sys


def solution(N,IC,A):
    graph = [[] for i in range(N + 1)]
    # make Graph
    for i in range(IC):
        graph[A[i][0]].append(A[i][1])
        graph[A[i][1]].append(A[i][0])
    # 방문체크 배열(0번째 인덱스 사용x)
    visited = [False] * (N + 1)
    # 1번째 인덱스 스택에 추가
    stack = [1]
    while stack:
        # 스택의 최근값 꺼내서 방문처리
        cur = stack.pop()
        visited[cur] = True
        # 최근값의 자식노드를 스택에 추가
        for i in graph[cur]:
            if not visited[i]:
                stack.append(i)

    count = 0
    for i in visited:
        if i:
            count += 1
    count -= 1
    print(count)


def getInputs():
    N = int(sys.stdin.readline())
    IC = int(sys.stdin.readline())
    A = []
    # N = 7
    # IC = 6
    # A = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]
    for _ in range(IC):
        A.append(list(map(int, sys.stdin.readline().split())))
    return N, IC, A


def main():
    N, IC, A = getInputs()
    solution(N,IC,A)



main()