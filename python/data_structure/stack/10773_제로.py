inp = int(input())


def getInputs(inp):
    ips = []
    for i in range(inp):
        ips.append(input())
    return ips


def isOpen(a):
    return True if a == "(" or a == "[" else False


def isClose(a):
    return True if a == ")" or a == "]" else False


def isPair(a, b):
    if a == "(":
        return True if b == ")" else False
    elif a == "[":
        return True if b == "]" else False
    return False


def isOk(a):
    stack = []
    for i in a:
        val=0
        if isOpen(i):
            stack.append(i)
        elif not len(stack):
            return "NO"
        elif isClose(i):
            val = stack.pop()
            if not isPair(val, i):
                return "NO"
    if len(stack):
        return "NO"
    return "YES"


def solution(ips):
    for i in ips:
        print(isOk(i))



inputs = getInputs(inp)

solution(inputs)