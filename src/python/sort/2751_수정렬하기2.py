def heapSort(arr):
    # heapify
    heap = []
    for i in arr:
        heap.append(i)
        if len(heap) == 1:
            continue
        cur = len(heap) - 1
        parent = (cur - 1) // 2
        while heap[cur] > heap[parent] and parent >= 0:
            heap[cur], heap[parent] = heap[parent], heap[cur]
            cur = parent
            parent = (cur - 1) // 2
    # sort
    for j in range(len(heap) - 1, 1, -1):
        root = 0
        heap[root], heap[j] = heap[j], heap[root]
        while root < (j) // 2:
            left = root * 2 + 1
            right = left + 1
            largest = left if heap[left] > heap[right] else right
            if heap[largest] > heap[root] and largest < j:
                heap[root], heap[largest] = heap[largest], heap[root]
                root = largest
            else:
                break
    print()
    for j in heap:
        print(j)

import sys

def solution():
    IC = int(input())
    arr = []
    for _ in range(IC):
        arr.append(int(sys.stdin.readline()))
    for i in sorted(arr):
        sys.stdout.write(str(i)+'\n')

solution()
    #     arr.append(int(input()))
    # heapSort(arr)


# arr = [124, 124, 512, 65784, 7, 34, 323, 515, 2, 325, 125, 4, 12515, 4]
# heapSort(arr)

# heapSort([12421, 51, 5, 125, 12, 512, 4, 13, 1, 23, 24, 124])
