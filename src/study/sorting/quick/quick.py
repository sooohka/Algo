# 기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 알고리즘
# 첫번째 인덱스에서 부터 비교하고 또 마지막 인덱스에서부터 비교한다.
# 단 두 인덱스가 교차되면 피벗값을 작은 데이터의 위치와 바꾸고 그 위치에서 진행
# 이렇게 피벗의 위치가 fix되면 피벗의 위치보다 왼쪽에 있는 데이터는 모두 피벗보다 작고
# 오른쪽에 있는 데이터는 모두 피벗보다 크다는 특징이 있음

# 시간 복잡도는 평균 O(N(logN)) 최악의 경우 O(n^2)


def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        # right
        while right >= start + 1 and arr[pivot] <= arr[right]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quickSort(arr, pivot, right - 1)
    quickSort(arr, right + 1, end)


arr = [2, 1, 5, 7, 3, 4, 6, 8, 9]
quickSort(arr, 0, len(arr) - 1)
print(arr)