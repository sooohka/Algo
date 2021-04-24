count = 0


def solution(n, k):
    global count
    if n == 1:
        return count
    elif n % k == 0:
        count += 1
        return solution(n // k, k)
    else:
        count += 1
        return solution(n - 1, k)


print(solution(25, 3))
