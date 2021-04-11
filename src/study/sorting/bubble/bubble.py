def bubbleSort(arr):
    for i in range(len(arr)):
        small = i
        for j in range(i, len(arr)):
            if arr[small] > arr[j]:
                small = j
        arr[i], arr[small] = arr[small], arr[i]


arr = [12, 31, 24, 14, 24, 1, 4, 125, 1, 51, 25, 313, 1, 5, 1, 7, 71, 7, 17, 37, 274273]
bubbleSort(arr)
print(arr)