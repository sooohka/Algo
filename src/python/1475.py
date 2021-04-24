import sys, math


def solution(n):
    arr = list(map(lambda k: k, list(n)))
    dict = {}
    for i in arr:
        if i == "9":
            i = "6"
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    try:
        dict["6"] = math.ceil(dict["6"] / 2)
    except:
        dict["6"] = 0
    return dict[max(dict, key=lambda k: dict[k])]
    


print(solution(sys.stdin.readline().strip()))
