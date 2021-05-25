import sys


def getInput():
    N = int(sys.stdin.readline())
    switches = [None]
    switches.extend(list(map(int, sys.stdin.readline().split())))
    M = int(sys.stdin.readline())
    kids = []
    for _ in range(M):
        kids.append(list(map(int, sys.stdin.readline().split())))
    return switches, kids


def boy(switches, loc):
    while loc < len(switches):
        if switches[loc] == 1:
            switches[loc] = 0
        elif switches[loc] == 0:
            switches[loc] = 1
        loc += loc


def girl(switches, loc):
    val = 0
    while loc - val >= 0 and loc + val < len(switches):
        if switches[loc + val] == switches[loc - val]:
            if switches[loc + val] == 1:
                switches[loc + val] = 0
            elif switches[loc + val] == 0:
                switches[loc + val] = 1
            if val == 0:
                val += 1
                continue
            if switches[loc - val] == 1:
                switches[loc - val] = 0
            elif switches[loc - val] == 0:
                switches[loc - val] = 1
        val += 1


def solution():
    switches, kids = getInput()
    for i in range(len(kids)):
        # boy
        if kids[i][0] == 1:
            boy(switches, kids[i][1])
        # girl
        if kids[i][0] == 1:
            girl(switches, kids[i][1])

    for i in range(1, len(switches)):
        if i % 20 == 0:
            sys.stdout.write("\n")
        sys.stdout.write(str(switches[i]) + " ")


solution()
