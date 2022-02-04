# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

num = int(input())
sosu = list(map(int, input().split(" ")))


def isPrime(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def func(n, sosu):
    count = 0
    for i in sosu:
        if isPrime(i):
            count += 1
    return count


print(func(num, sosu))
