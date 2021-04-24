import sys


def getInput():
    row, col = map(int, sys.stdin.readline().split())
    IC = int(sys.stdin.readline())
    stores = []
    for _ in range(IC + 1):
        l, d = map(int, sys.stdin.readline().split())
        # 북
        if l == 1:
            stores.append(row - d)
        # 서
        elif l == 3:
            stores.append(row + d)
        # 남
        elif l == 2:
            stores.append(row + col + d)
        # 동
        elif l == 4:
            stores.append(row + col + row + (col - d))
    myLoc = stores.pop()
    mapSize = 2 * (row + col)
    return stores, myLoc, mapSize


def solution():
    stores, myLoc, mapSize = getInput()
    sum = 0
    for i in range(len(stores)):
        temp = abs(stores[i] - myLoc)
        temp2 = abs(mapSize - abs(stores[i] - myLoc))
        sum += temp if temp < temp2 else temp2
    return sum


print(solution())
