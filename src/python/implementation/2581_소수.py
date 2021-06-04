a = int(input())
b = int(input())


def isPrime(n):
    i = 2
    if n == 1:
        return 0
    if n == 2:
        return 1
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1


def sumPrimes(a, b):
    value = 0
    least = 0
    for i in range(a, b + 1):
        if isPrime(i):
            if least == 0:
                least = i
            value += i
    if value == 0:
        print(-1)
    else:
        print(value)
        print(least)


sumPrimes(a, b)
