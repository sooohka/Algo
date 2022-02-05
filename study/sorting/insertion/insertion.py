# 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 알고리즘
# 배열의 인덱스를 올려가면서 원소를 하나씩 비교해 위치를 판단하는 알고리즘
# 길이가 n인 배열에서 m번째 인덱스와 그 앞에있는 인덱스들 비교하여 정렬하는 알고리즘 (n>m)
# m번째 인덱스가 그 앞에 있는 인덱스보다 큰경우 while문 break
# 1.    [1,5,2,7,3,4,6,8,9]
#     - 첫번째 시도에서 1번째 인덱스와 그 앞에있는 인덱스들을 비교하는데
#       지금은 0번째 인덱스밖에 없음으로 0번째 인덱스가 1번쨰 인덱스보다 작음으로 그냥둔다
#     - 결과 : [1,5,2,7,3,4,6,8,9]
# 2.     [1,5,2,7,3,4,6,8,9]
#     - 두번째 시도에서 2번쨰 인덱스와 그 앞에 있는 인덱스들을 비교하는데
#       우선 2번쨰 인덱스 2와 1번째 인덱스 5를 비교했을때 2가 더 작음으로 그 둘의 위치르 변경한다
#       이후 0번쨰 인덱스와도 비교하는데 0번째 인덱스가 더작음으로 그냥 둔다(while문 break)
#     - 결과 : [1,2,5,7,3,4,6,8,9]
# 일반적으로 while문을 두개 중첩시키기 때문에 시간복잡도는 O(n^2)이지만
# break문을 통해 정렬이 되있는상태라면 바로 break시키기 때문에 즉
# 이미 거의다 정렬이 되어있는 배열을 정렬시킬때 매우 빠르게 동작한다


def insertion(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


arr = [4, 24, 15, 12, 4, 1, 16]
print(insertion(arr))