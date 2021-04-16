import sys


def getInput():
    IC = int(sys.stdin.readline())
    arr = [0]
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    return IC, arr


def solution():
    IC, arr = getInput()
    cache = [0 for _ in range(301)]
    for i in range(IC):
        cache[i] = arr[i]
    cache[1] = arr[1]
    cache[2] = cache[1] + arr[2]
    cache[3] = (
        cache[1] + arr[3] if cache[1] + arr[3] > cache[2] + arr[3] else cache[2] + arr[3]
    )  # 한칸 두칸 혹은 두칸 한칸
    for i in range(4, 301):
        # 두칸 한칸 한칸
        cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 4]
        # 한칸 두칸 한칸
        if cache[i] < cache[i - 1] + cache[i - 3] + cache[i - 4]:
            cache[i] = cache[i - 1] + cache[i - 3] + cache[i - 4]
            # 한칸 한칸 두칸
        if cache[i] < cache[i - 2] + cache[i - 3] + cache[i - 4]:
            cache[i] = cache[i - 2] + cache[i - 3] + cache[i - 4]
    print(cache[IC])


# cache(i)=cache(i-1)+cache(i-2)+cache(i-4) 두칸 한칸 한칸
# cache(i)=cache(i-1)+cache(i-3)+cache(i-4) 한칸 두칸 한칸
# cache(i)=cache(i-2)+cache(i-3)+cache(i-4) 한칸 한칸 두칸
solution()