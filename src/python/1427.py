import sys


def heapSort(arr):

    # heapify
    for i in range(1, len(arr)):
        cur = i
        parent = (i - 1) // 2
        while arr[cur] > arr[parent] and parent >= 0:
            arr[cur], arr[parent] = arr[parent], arr[cur]
            cur = parent
            parent = (cur - 1) // 2
    # sort
    for i in range(len(arr) - 1, 0, -1):
        root = 0
        if arr[root]>arr[i]:
            arr[root], arr[i] = arr[i], arr[root]
        while root < (i - 1) // 2:
            left = root * 2 + 1
            right = left + 1
            larger = left if arr[left] > arr[right] else right
            if arr[root] < arr[larger]:
                arr[larger], arr[root] = arr[root], arr[larger]
                root = larger
            else:
                break



def solution():
    input = sys.stdin.readline()
    arr = []
    for i in range(len(input) - 1):
        arr.append(int(input[i]))
    heapSort(arr)
    for k in range(len(arr)-1,-1,-1):
        sys.stdout.write(str(arr[k]))

solution()

# heapSort(
#     [124, 12, 215, 12, 135, 135, -4, 515, 1, 2, 12, 3, 12, 5, 15, 2, 163, 4, 0, 90, 2, 78676, 1]
# )
