import sys

input = sys.stdin.readline

maxN = 0


def getInput():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(int(input()))
    return arr


def makeTree(tree, node, arr, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    mid = (start + end) // 2
    left = makeTree(tree, node * 2, arr, start, mid)
    right = makeTree(tree, node * 2 + 1, arr, mid + 1, end)
    tree[node] = min(left, right)
    return tree[node]


def find(tree, node, arr, start, end):
    global maxN
    tmp = tree[node] * (end - start + 1)
    if maxN < tmp:
        maxN = tmp
    if start == end:
        return
    mid = (start + end) // 2
    #기준을 잡는법
    find(tree, node * 2, arr, start, mid)
    find(tree, node * 2 + 1, arr, mid + 1, end)


def solution():
    global maxN
    arr = getInput()
    tree = [None] * (4 * len(arr))
    makeTree(tree, 1, arr, 0, len(arr) - 1)
    find(tree, 1, arr, 0, len(arr) - 1)
    print(maxN)


solution()
7
2
1
1
5
4
1
3