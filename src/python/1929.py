a = list(map(int, input().split(" ")))


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def ans(a, b):
    for i in range(a, b + 1):
        if isPrime(i):
            print(i)


ans(a[0], a[1])
