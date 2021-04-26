import sys


def solution(a, b):
    A, B = a, b
    # 비가 항상 더크게
    if a < b:
        b, a = a, b
    # 유클리드 호재
    while b != 0:
        r = a % b
        a = b
        b = r
    print(a)
    print((A * B) // a)
    return


a, b = map(int, sys.stdin.readline().split())
solution(a, b)
