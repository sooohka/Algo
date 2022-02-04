def selectionSort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i + 1, len(arr)):
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]
    return arr


def solution(arr):
    selectionSort(arr)
    for i in arr:
        print(i)


IC = int(input())
arr = []
for i in range(IC):
    arr.append(int(input()))


solution(arr)