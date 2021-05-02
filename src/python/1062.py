import sys

maxNum = 0


def getInput():
    n, k = map(int, sys.stdin.readline().split())
    # 읽어야되는 배열 기본적으로 acnti읽을수 있어야됨으로 제외함
    word = []
    # 가르칠 수 있는 글자들
    strs = []
    for _ in range(n):
        a = list(set(sys.stdin.readline().strip()))
        a.remove("a")
        a.remove("c")
        a.remove("n")
        a.remove("t")
        a.remove("i")
        if len(a) > k - 5:
            continue
        word.append("".join(a))
        strs += a
    strs = sorted(set(strs))
    return n, k - 5, word, strs


def dfs(word, strs, visited, temp, length, cur):
    global maxNum
    if len(temp) == length:
        count = 0
        temp = "".join(temp)
        for i in word:
            if temp.find(i) != -1:
                count += 1
        if maxNum < count:
            maxNum = count
    else:
        for i in range(cur, len(strs)):
            if not visited[strs[i]]:
                temp.append(strs[i])
                visited[strs[i]] = True
                dfs(word, strs, visited, temp, length, i)
                temp.pop()
                visited[strs[i]] = False


def solution():
    n, k, word, strs = getInput()
    z = len(strs)
    length = z if z < k else k
    temp = []
    visited = {}
    for i in strs:
        visited[i] = False
    # 가르칠수 있는 단어가 5개 미만이면 안됨
    if k < 0:
        return 0
    dfs(word, strs, visited, temp, length, 0)
    return maxNum


print(solution())

# 1 7
# antabbtica
# output: 0
# correct answer: 1

# 2 7
# antaatica
# antabtica
# output: 0
# correct answer: 2

# 1 7
# antabctica
# output: 0
# correct answer: 1
