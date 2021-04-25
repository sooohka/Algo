import sys


def solution(n):
    strs = ""
    n += 1
    while n > 0:
        if n % 2 == 0:
            strs = "4" + strs
        else:
            strs = "7" + strs
        n //= 2
    strs = strs[1:]
    print("".join(strs))


solution(int(sys.stdin.readline()))