import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    return IC, arr


def solution():
    IC, arr = getInput()
    strs = ""
    stack = []
    for i in range(len(arr) - 1, -1, -1):
        while stack and arr[i] > stack[len(stack) - 1]:
            stack.pop()
        if not stack:
            strs = "-1 " + strs
            stack.append(arr[i])
            continue
        strs = str(stack[len(stack) - 1]) + " " + strs
        stack.append(arr[i])


def sol():
    IC, arr = getInput()
    res = [-1] * IC
    stack = []
    i = 0
    while i < IC:
        while stack and arr[stack[-1]] < arr[i]:
            res[stack[-1]] = arr[i]
            stack.pop()
        stack.append(i)
        i += 1
    return " ".join(map(str, res))


sys.stdout.write(sol())
# solution()