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


def makeMinTree(tree, node, arr, start, end):
    if start == end:
        tree[node][0] = arr[start]
        return tree[node][0]
    mid = (start + end) // 2
    left = makeMinTree(tree, node * 2, arr, start, mid)
    right = makeMinTree(tree, node * 2 + 1, arr, mid + 1, end)
    tree[node][0] = min(left, right)
    return tree[node][0]


def makeMaxTree(tree, node, arr, start, end):
    if start == end:
        tree[node][1] = arr[start]
        return tree[node][1]
    mid = (start + end) // 2
    left = makeMaxTree(tree, node * 2, arr, start, mid)
    right = makeMaxTree(tree, node * 2 + 1, arr, mid + 1, end)
    tree[node][1] = max(left, right)
    return tree[node][1]


def find(tree, node, arr, start, end, begin, finish):
    if end < begin or start > finish:
        return (1000000000, 1)
    if begin <= start and end <= finish:
        return (tree[node][0], tree[node][1])
    mid = (start + end) // 2
    leftMin, leftMax = find(tree, node * 2, arr, start, mid, begin, finish)
    rightMin, rightMax = find(tree, node * 2 + 1, arr, mid + 1, end, begin, finish)
    return (min(leftMin, rightMin), max(leftMax, rightMax))


def solution():
    arr, ran = getInput()
    tree = [[1000000000, 1] for _ in range(4 * len(arr))]
    makeMinTree(tree, 1, arr, 0, len(arr) - 1)
    makeMaxTree(tree, 1, arr, 0, len(arr) - 1)
    for i in ran:
        print(" ".join(list(map(str, find(tree, 1, arr, 0, len(arr) - 1, i[0] - 1, i[1] - 1)))))


solution()
