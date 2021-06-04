import sys


def getInput():
    # M 변경횟수 K합구하는 횟수
    N, M, K = map(int, sys.stdin.readline().split())
    arr = []
    op = []
    # N초기화
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))
    # 연산
    for _ in range(M + K):
        op.append(list(map(int, sys.stdin.readline().split())))
    return N, arr, op


def makeTree(node, tree, start, end, arr):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = makeTree(node * 2, tree, start, mid, arr)
    right = makeTree(node * 2 + 1, tree, mid + 1, end, arr)
    tree[node] = left + right
    return tree[node]


def find(node, tree, start, end, begin, finish):
    if start > finish or end < begin:
        return 0
    if begin <= start and finish >= end:
        return tree[node]
    mid = (start + end) // 2
    left = find(node * 2, tree, start, mid, begin, finish)
    right = find(node * 2 + 1, tree, mid + 1, end, begin, finish)
    return left + right


def change(node, tree, start, end, index, changer):
    if not (start <= index and index <= end):
        return
    tree[node] += changer
    if start == end:
        return
    mid = (start + end) // 2
    change(node * 2, tree, start, mid, index, changer)
    change(node * 2 + 1, tree, mid + 1, end, index, changer)


def solution():
    N, arr, op = getInput()
    tree = [0] * (N * 4)
    makeTree(1, tree, 0, len(arr) - 1, arr)
    for i in op:
        # 원소 바꾸기
        if i[0] == 1:
            changer = i[2] - arr[i[1] - 1]
            arr[i[1] - 1] = i[2]
            change(1, tree, 0, len(arr) - 1, i[1] - 1, changer)
            print(tree)
        # 값 출력
        elif i[0] == 2:
            print(find(1, tree, 0, len(arr) - 1, i[1] - 1, i[2] - 1))


solution()
