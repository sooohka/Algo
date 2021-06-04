import sys


def rec(i, n):
    if i == n:
        return
    strs = "____" * i
    sys.stdout.write(strs + '"재귀함수가 뭔가요?"\n')
    sys.stdout.write(strs + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n')
    sys.stdout.write(strs + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n")
    sys.stdout.write(strs + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n')
    return rec(i+1,n)

def rec2(n):
    if n < 0:
        return
    strs = "____" * n
    sys.stdout.write(strs + "라고 답변하였지.\n")
    return rec2(n - 1)


def solution(n):
    sys.stdout.write("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n")
    rec(0, n)
    strs = "____" * n
    sys.stdout.write(strs + '"재귀함수가 뭔가요?"\n')
    sys.stdout.write(strs+'"재귀함수는 자기 자신을 호출하는 함수라네"\n')
    rec2(n)

    return


solution(int(sys.stdin.readline()))