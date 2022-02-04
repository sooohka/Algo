import sys


def solution(s):
    stack = []
    for i in range(len(s)):
        # 닫는괄호 아니면 스택에 추가
        if s[i] != ")":
            if s[i] == "(":
                stack.append(s[i])
                continue
            if i < len(s) - 1 and s[i + 1] == "(":
                stack.append(int(s[i]))
                continue
            else:
                stack.append(1)
                continue
        # 닫는괄호
        else:
            temp = 0
            # 여는괄호 나올때까지
            while stack[-1] != "(":
                temp += stack.pop()
            # 여는괄호 팝
            stack.pop()
            stack.append(stack.pop() * temp)
    return sum(stack)


print(solution(sys.stdin.readline().strip()))

# 메모리초과
# 값을 스택에 저장할때 길이를 저장해야함..