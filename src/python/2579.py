import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = [0]
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return IC, arr


def solution():
    IC, arr = getInput()
    cache = [0 for _ in range(IC + 1)]
    # 한칸 두칸 혹은 두칸 한칸
    cache[1] = arr[1]
    try:
        cache[2] = arr[2] + arr[1]
        cache[3] = arr[3] + cache[1] if arr[3] + cache[1] > arr[3] + arr[2] else arr[3] + arr[2]
    except:
        return arr[2] + arr[1] if IC==2 else arr[1]
    for i in range(4, IC + 1):
        # 마지막에 두칸
        cache[i] = arr[i] + cache[i - 2]
        # 마지막에 한칸
        if cache[i] < arr[i] + arr[i - 1] + cache[i - 3]:
            cache[i] = arr[i] + arr[i - 1] + cache[i - 3]
    return (cache[IC])


# 모든 과정을 생각하지말고 무조건 현재 위치에서 발생할 수 있는 상황에 대해서만 생각하자
print(solution())