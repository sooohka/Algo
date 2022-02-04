# 모든 원소가 0과 자연수인 경우에만 사용가능
# 배열의 인덱스 값중 가장 큰값(k)을 기준으로 그 큰값(k)을 길이로 하는 배열을 만든다
# 루프를 돌면서 배열의 인덱스의 값에 해당하는 새로만든 배열의 인덱스를 증가시킨다
# 최종적으로 만든 배열을 그대로 이어붙이면 정렬됨
# 시간복잡도는 O(n+k)이지만 낭비되는 공간이 많이때문에 공간복잡도가 높다.


def counting(arr):
    new = [0] * (max(arr) + 1)
    ans = []
    for i in arr:
        new[i] += 1
    arr.clear()
    for k in range(len(new)):
        while new[k] > 0:
            arr.append(k)
            new[k] -= 1
    return ans


arr = [4, 12, 3, 14, 15, 12, 512, 31, 411, 1, 1, 1, 2, 3, 1, 4, 2, 4, 4, 4]
counting(arr)
print((arr))
