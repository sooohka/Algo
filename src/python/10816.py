import sys


def getInputs():
    N = sys.stdin.readline()
    A = list(map(int, sys.stdin.readline().split()))
    M = sys.stdin.readline()
    B = list(map(int, sys.stdin.readline().split()))
    return N, A, M, B


def solution():
    N, A, M, B = getInputs()
    C = {}
    for i in A:
        try:
            C[i] += 1
        except:
            C[i] = 1
    strs = ""
    for i in B:
        try:
            strs += str(C[i]) + " "
        except:
            strs += "0 "
    sys.stdout.write(strs)


solution()
