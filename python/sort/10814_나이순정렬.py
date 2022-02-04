import sys


def getInput():
    IC = int(sys.stdin.readline())
    A = []
    for i in range(IC):
        a, b = sys.stdin.readline().split()
        A.append((int(a), b))

    return IC, A


def solution():
    IC, A = getInput()
    A.sort(key=lambda k: (k[0]))
    strs = ""
    for i in A:
        strs += str(i[0]) + " " + i[1] + "\n"
    sys.stdout.write(strs)


solution()