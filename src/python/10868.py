import sys


def getInput():
    N, M = map(int, sys.stdin.readline().split())
    arr = []
    ran = []
    for _ in range(N):
        arr.append(int(sys.stdin.readline()))
    for _ in range(M):
        ran.append(list(map(int, sys.stdin.readline().split())))
    return arr, ran


def makeTree(tree, node, arr, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = makeTree(tree, node * 2, arr, start, mid)
    right = makeTree(tree, node * 2 + 1, arr, mid + 1, end)
    tree[node] = min(left, right)
    return tree[node]


def find(tree, node, start, end, begin, finish):
    if begin > end or start > finish:
        return 1000000000
    if begin <= start and end <= finish:
        return tree[node]
    mid = (start + end) // 2
    left = find(tree, node * 2, start, mid, begin, finish)
    right = find(tree, node * 2 + 1, mid + 1, end, begin, finish)
    return min(left, right)


def solution():
    arr, ran = getInput()
    tree = [None] * (4 * len(arr))
    makeTree(tree, 1, arr, 0, len(arr) - 1)
    for i in ran:
        sys.stdout.write(str((find(tree, 1, 0, len(arr) - 1, i[0] - 1, i[1] - 1))) + "\n")


solution()
