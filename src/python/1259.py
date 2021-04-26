import sys


def solution(strs):
    for i in range(len(strs) // 2):
        if strs[i] != strs[len(strs) - i - 1]:
            print("no")
            return
    print("yes")


while True:
    temp=sys.stdin.readline().strip()
    if temp=='0':
        break
    solution(temp)