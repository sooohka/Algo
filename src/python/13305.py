import sys


def getInput():
    IC = int(sys.stdin.readline())
    dist = list(map(int, sys.stdin.readline().split()))
    gas = list(map(int, sys.stdin.readline().split()))
    return IC, dist, gas


# 4
# 2 3 1
# 5 2 4 1
def solution():
    IC, dist, gas = getInput()
    # 마지막 도시의 주유소 필요없음
    gas.pop()
    cost = 0
    i = 0
    while i < len(dist):
        cost += gas[i] * dist[i]
        cur = i
        for j in range(cur + 1, len(dist)):
            # 다음 도시의 가스보다 현 도시의 가스가 싸다면
            if gas[cur] < gas[j]:
                cost += dist[j] * gas[cur]
                # i값 갱신
                i = j
            else:
                break
        i += 1
    return cost


# print(solution())

