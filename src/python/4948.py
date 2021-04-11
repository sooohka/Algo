def getInputs():
    num = []
    while True:
        a = int(input())
        if a == 0:
            break
        num.append(a)
    return num


def getPrimeCount(n):
    count = 0
    arr = []
    for i in range(n, 2 * n + 1):
        arr[i] True
    i = 2
    while i * i <= n:
        if arr[i]:
            j = i + i
            while j < n:
                arr[j] = False
                j += i
        i += 1
    for k in arr:
        if k:
            count += 1
    return count


def getAns(N):
    for i in N:
        print(getPrimeCount(i))


getAns(getInputs())
