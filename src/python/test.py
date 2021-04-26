import sys


def solution(arr):
    # True ascending
    flag = True
    if arr[0] > arr[1]:
        flag = False
    # ascending
    if flag:
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                continue
            print("mixed")
            return
        print("ascending")
    else:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                continue
            print("mixed")
            return 
        print("descending")



solution(list(map(int, sys.stdin.readline().split())))
