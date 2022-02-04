import sys


def getInput():
    IC = int(sys.stdin.readline())
    strs = sys.stdin.readline().strip()
    return IC, strs


def pow(a, b):
    tmp = 1
    for _ in range(b):
        tmp *= a
    return tmp


def solution():
    IC, strs = getInput()
    dict = {}
    count = 0
    for i in range(0, 26):
        dict[chr(97 + i)] = i + 1
    for i in range(len(strs)):
        count += dict[strs[i]] * pow(31, i)
    print(count % 1234567891)


solution()