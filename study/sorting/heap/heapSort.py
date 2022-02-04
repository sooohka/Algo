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


arr = [1,4,4,124,2]
print("before Sort:", arr)
heapSort(arr)
print("after Sort:", arr)
