# 선택정렬
# n개의 배열에서
# - 범위를 정해 그 범위에 있는 원소중 가장 작은 원소를 범위의 맨앞에 있는 원소와 위치를 바꾼다
# 1. [8,5,2,7,3,4,6,1,9]
#     - 첫번째 시도에서 범위는 n개의 배열이기 때문에 n이고 0번째 인덱스에서 시작한다.
#     1이 가장 작기때문에 1과 8의 위치를 바꾼다.
#     - 결과 : [1,5,2,7,3,4,6,8,9]
# 2.  [1,5,2,7,3,4,6,8,9]
#     - 두번째 시도에서 하나의 원소를 소팅했음으로 범위는 n-1이며 1번째 인덱스에서 시작한다.
#     1을 제외하고 2가 가장 작기때문에 1번쨰 인덱스인 5와 위치를 바꾼다
#     - 결과 : [1,2,5,7,3,4,6,8,9]
# 3. [1,2,5,7,3,4,6,8,9]
#     - 세번째 시도에서 범위는 n-2이고 2번째 인덱스에서 시작한다.
#     1,2를 제외하고 3이 가장 작기 때문에 2번쨰 인덱스인 5와 위치를 바꾼다
#     - 결과 [1,2,3,7,5,4,6,8,9]
# 4. 이런식으로 진행하다보면 정렬이 완성된다.
# 5. 일반적으로 while문을 두개 중첩시킴으로 시간복잡도는 O(n^2)이다.


def selectionSort(arr):
    for i in range(len(arr)):
        smallIndex = i
        for j in range(i + 1, len(arr)):
            if arr[smallIndex] > arr[j]:
                smallIndex = j
        arr[i], arr[smallIndex] = arr[smallIndex], arr[i]
    return arr


# print(selectionSort([4, 12, 3, 5, 1, 25, 12, 5, 6, 1]))


# 5
# 20 10 35 30 7


# def quickSort(arr, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and arr[left] <= arr[pivot]:
#             left += 1
#         while right >= start + 1 and arr[right] >= arr[pivot]:
#             right -= 1
#         if left > right:
#             arr[pivot], arr[right] = arr[right], arr[pivot]
#             break
#         else:
#             arr[left], arr[right] = arr[right], arr[left]
#     quickSort(arr, pivot, right - 1)
#     quickSort(arr, right + 1, end)


IC = int(input())
for _ in range(IC):
    str=input()
    for j in len(str):
