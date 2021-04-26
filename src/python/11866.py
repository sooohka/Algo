import sys


def solution(a, b):
    arr = []
    for i in range(1, a + 1):
        arr.append(i)
    # 1 2 4 5 7
    kill = b - 1
    print("<", end="")
    for _ in range(len(arr)):
        if len(arr) != 1:
            print(arr.pop(kill), end=", ")
        elif len(arr) == 1:
            print(arr.pop(kill), end="")
        kill += b - 1
        while kill > len(arr) - 1:
            if not arr:
                print(">")
                return
            kill = kill - len(arr)


a, b = map(int, sys.stdin.readline().split())
solution(a, b)
