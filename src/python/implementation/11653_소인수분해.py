num = int(input())

# 2 72
# 2 36
# 2 18
# 3 9
#   3
def getsoinsu(n):
    i = n // 2
    while i > 0:
        if n % i == 0:
            print(n // i)
            n = i
        i -= 1


getsoinsu(num)