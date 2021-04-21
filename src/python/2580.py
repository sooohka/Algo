import sys

def visual(arr):
    print()
    for i in range(len(arr)):
        if i>0 and  i%3==0:
            print()
        for j in range(len(arr[i])):
            if j>0 and j%3==0:
                print(end=" ")
            print(arr[i][j],end=" ")
        print()

def getInput():
    arr = []
    for _ in range(9):
        arr.append(list(map(int, sys.stdin.readline().split())))
    return arr




visual(getInput())

