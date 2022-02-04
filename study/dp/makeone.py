def makeOne(n):
    cache = [0 for _ in range(30001)]
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + 1
        if i % 2 == 0:
            cache[i] = cache[i] if cache[i] < cache[i // 2] + 1 else cache[i // 2] + 1
        if i % 3 == 0:
            cache[i] = cache[i] if cache[i] < cache[i // 3] + 1 else cache[i // 3] + 1
        if i % 5 == 0:
            cache[i] = cache[i] if cache[i] < cache[i // 5] + 1 else cache[i // 5] + 1
    return cache[n]


def antWarrior(arr):
    cache = [0 for _ in range(100)]
    cache[0] = arr[0]
    cache[1] = arr[1]
    for i in range(2, len(arr)):
        if cache[i - 2] + arr[i] > cache[i - 1]:
            cache[i] = cache[i - 2] + arr[i]
        else:
            cache[i] = cache[i - 1]
    return cache[len(arr) - 1]


def tile(n):
    cache = [0 for _ in range(n)]
    cache[0] = 1
    cache[1] = 3
    for i in range(2, n):
        cache[i] = 2 * cache[i - 2] + cache[i - 1]
    return cache[n - 1]


def cash(arr, m):
    cache = [10001 for _ in range(10001)]
    for i in range(len(arr)):
        cache[arr[i]] = 1
    for j in range(len(arr) + 1, m + 1):
        for k in arr:
            t = cache[j - k] + 1
            if cache[j] > t:
                cache[j] = t
    if cache[m] != 10001:
        return cache[m]
    return -1


def goldMine(n, m, arr):
    cache = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        cache[i][0] = arr[i][0]
    for i in range(1, m):
        for j in range(n):
            # 판별
            if j > 0:
                cache[j][i] = cache[j - 1][i - 1] + arr[j][i]
            if cache[j][i] < cache[j][i - 1] + arr[j][i]:
                cache[j][i] = cache[j][i - 1] + arr[j][i]
            if j < n - 1 and cache[j][i] < cache[j + 1][i - 1] + arr[j][i]:
                cache[j][i] = cache[j + 1][i - 1] + arr[j][i]

    max = 0
    for k in range(n):
        if cache[k][m - 1] > max:
            max = cache[k][m - 1]
    return max


def soldier():
    return 

# n, m = 3, 4
# arr = [[1, 3, 3, 2], [2, 1, 4, 1], [0, 6, 4, 7]]  # 19
# n, m = 4, 4
# arr = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
# 1 3 3 2
# 2 1 4 1
# 0 6 4 7
print(goldMine(n, m, arr))
