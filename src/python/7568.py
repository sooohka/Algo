import sys


def getInput():
    IC = int(sys.stdin.readline())
    humans = []
    for _ in range(IC):
        humans.append(list(map(int, sys.stdin.readline().split())))
    return IC, humans


def solution():
    IC, humans = getInput()
    for i in range(len(humans)):
        k = 1
        for j in range(len(humans)):
            if humans[i][0] < humans[j][0] and humans[i][1] < humans[j][1]:
                k += 1
        print(k,end=' ')


solution()