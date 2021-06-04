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
        if not isOpen(i) and not isClose(i):
            continue
        val = 0
        if isOpen(i):
            stack.append(i)
        elif not len(stack):
            return "no"
        elif isClose(i):
            val = stack.pop()
            if not isPair(val, i):
                return "no"
    if len(stack):
        return "no"
    return "yes"


def solution(ips):
    for i in ips:
        print((isOk(i)))


strings = []
while 1:
    string = input()
    if string == ".":
        break
    strings.append(string)

solution(strings)

# So when I die (the [first] I will see in (heaven) is a score list).[ first in ] ( first out ).Half Moon tonight (At least it is better than no Moon at all].A rope may form )( a trail in a maze.Help( I[m being held prisoner in a fortune cookie factory)].([ (([( [ ] ) ( ) (( ))] )) ]). ..
