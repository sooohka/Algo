import sys

count = 0


def rec(arr):
    global count
    temp = 0
    if len(arr) < 2:
        return int(arr[0]) % 3
    for i in arr:
        temp += int(i)
    count += 1
    return rec(str(temp))


def solution(n):
    temp = rec(n)
    sys.stdout.write(str(count) + "\n")
    if temp == 0:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


solution(sys.stdin.readline().strip())
