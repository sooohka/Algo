import sys

sub = 1000000000000


def getInput():
    N = int(sys.stdin.readline())
    arr = [[False]]
    for _ in range(N):
        temp = [False]
        temp += list(map(int, sys.stdin.readline().split()))
        arr.append(temp)
    return N, arr


def getPower(team, workers):
    power = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            power += workers[team[i]][team[j]]
            power += workers[team[j]][team[i]]
    return power


def dfs(team1, visited, workers, cur):
    global sub
    if len(team1) == (len(workers) // 2):
        # team나누기
        team2 = []
        for i in range(1, len(workers)):
            if i not in team1:
                team2.append(i)
        # 계산
        temp = abs(getPower(team1, workers) - getPower(team2, workers))
        if temp < sub:
            sub = temp
        return
    else:
        for i in range(cur, len(workers)):
            if not visited[i] and len(team1):
                team1.append(i)
                visited[i] = True
                dfs(team1, visited, workers, i)
                team1.pop()
                visited[i] = False
    return


def solution():
    N, workers = getInput()
    visited = [False] * (len(workers))
    visited[1] = True
    # 첫번째 인덱스가 1일때까지 돌면 딱 절반임
    team1 = [1]
    dfs(team1, visited, workers, 1)
    print(sub)


solution()
