import sys

# 1 7 19 37 61
def solution(n):
    temp = 1
    count = 1
    while True:
        if n <= temp:
            print(count)
            return
        temp += 6 * count
        count += 1


solution(int(sys.stdin.readline()))