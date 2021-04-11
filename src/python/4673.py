import sys
import time


def solution():
    arr = [False] * (10035 + 1)
    for i in range(1, 10000):
        temp = i
        while i > 0:
            temp += i % 10
            i //= 10
        arr[temp] = True
    for i in range(1, 10000):
        if not arr[i]:
            sys.stdout.write(str(i) + "\n")


solution()
start = time.time()
print(end - start)
end = time.time()
