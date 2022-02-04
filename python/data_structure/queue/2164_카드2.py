import sys
from collections import deque


def solution(n):
    arr = deque([])
    for i in range(1, n + 1):
        arr.append(i)
    while len(arr) != 1:
        # 젤위 버려
        arr.popleft()
        arr.append(arr.popleft())
    print(arr[0])


solution(int(sys.stdin.readline()))