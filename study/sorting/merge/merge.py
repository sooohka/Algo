def mergeSort(arr, start, end):
    if start < end:
        middle = (start + end) // 2
        mergeSort(arr, start, middle)
        mergeSort(arr, middle + 1, end)
        merge(arr, start, middle, end)


# 합치는 함수
def merge(arr, start, middle, end):
    new = []
    s = start
    m = middle + 1
    while s <= middle and m <= end:
        if arr[s] < arr[m]:
            print(start, middle, end, new)
            new.append(arr[s])
            s += 1
        else:
            new.append(arr[m])
            m += 1
    while s <= middle:
        new.append(arr[s])
        s += 1
    while m <= end:
        new.append(arr[m])
        m += 1
    print(start, middle, end, new)
    for i in range(len(new)):
        arr[start] = new[i]
        start += 1


arr = [12, 31, 24, 14, 24, 1, 4, 125, 1, 51, 25, 313, 1, 5, 1, 7, 71, 7, 17, 37, 274273]
# arr = [1, 23, 41, 5, 123, 12, 14, 3, 412, 1, 41241, 2, 35, 57, 676, 75, 7670]
print("before:", arr)
new = [0] * int(len(arr) - 1)
mergeSort(arr, 0, len(arr) - 1)
print("after:", arr)
