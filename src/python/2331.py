import sys


def getInput():
    A, P = map(int, sys.stdin.readline().split())
    return A, P


def solution():
    A, P = getInput()
    arr = [A]
    i = 0
    while True:
        temp = arr[i]
        t = 0
        while temp > 0:
            a = 1
            for _ in range(P):
                a *= temp % 10
            t += a
            temp //= 10
        for i in range(len(arr)):
            if arr[i] == t:
                return i
        arr.append(t)
        i += 1


print(solution())