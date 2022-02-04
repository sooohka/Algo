import sys

def countingSort(arr):
    temp = [0] * (max(arr) + 1)
    neg = [0] * (abs(min(arr)) + 1)
    bin = []
    most=0
    for i in arr:
        if i <= 0:
            continue
        temp[i] += 1
        if temp[i]>most:
            most=temp[i]
    for j in arr:
        if j > 0:
            continue
        neg[-j] += 1
        if neg[-j]>most:
            most=neg[-j]
    arr.clear()
    sum=0
    for i in range(len(neg) - 1, -1, -1):
        if neg[i] == most:
            bin.append(-i)
        while neg[i] > 0:
            arr.append(-i)
            sum+=(-i)
            neg[i] -= 1

    for i in range(len(temp)):
        if temp[i] == most:
            bin.append(i)
        while temp[i] > 0:
            arr.append(i)
            sum+=i
            temp[i] -= 1
    #print("bin",bin)
    if len(bin) > 1:
        return bin[1],sum
    return bin[0],sum


def solution():
    arr = []
    IC = int(sys.stdin.readline())
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    most,sum = countingSort(arr)
    print(round(sum / len(arr)))
    # 2
    print(arr[len(arr) // 2])
    # 3
    print(most)
    # 4
    print(arr[len(arr) - 1] - arr[0])


#solution()

#음수 배열 양수 배열을 따로 저장했는데 두배열에 모두 0을 저장했다!!
#배열 모두 0을 저장하지말고 한 배열에만 저장해야된다 



# 10 5
# 1 10 4 9 2 3 8 5 7 6

import sys

IC,max=map(int,input().split())
arr=map(int,input().split())
for i in arr:
    if i<max:
        sys.stdout.write(str(i)+' ')
