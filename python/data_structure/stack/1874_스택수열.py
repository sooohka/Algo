def solution(inputs):
    maxCount = inputs[0]
    stack = [0]
    current = 0
    str = ""
    for i in range(1, len(inputs)):
        if stack[len(stack) - 1] < inputs[i]:
            while stack[len(stack) - 1] != inputs[i]:
                current += 1
                if current > maxCount:
                    return "NO"
                stack.append(current)
                str += "+\n"
                # print("+")
            stack.pop()
            str += "-\n"
            # print("-")
        elif stack[len(stack) - 1] >= inputs[i]:
            # print("-")
            str += "-\n"
            while stack.pop() != inputs[i]:
                # print("-")
                str += "-\n"
                if not len(stack):
                    return "NO"
    return str


inputs = [8, 4, 3, 6, 8, 7, 5, 2, 1]
inputs2 = [5, 1, 2, 5, 3, 4]


def getInputs(a):
    inputs = [a]
    for _ in range(a):
        inputs.append(int(input()))
    return inputs

a=int(input())
qwer=getInputs(a);
print(solution(qwer))