import sys


def solution():
    IC = int(sys.stdin.readline())
    temp = [0] * 10001
    for _ in range(IC):
        temp[int(sys.stdin.readline())] += 1
    for i in range(10001):
        sys.stdout.write("%s\n" % i * temp[i])
solution()