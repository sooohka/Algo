def radixSort(arr):
    m = max(arr)
    digit = 0
    while m != 0:
        m //= 10
        digit += 1
    new = [[] for _ in range(10)]
    for i in range(digit):
        for j in arr:
            index = (j // (10 * i)) % 10 if i else j % 10
            new[index].append(j)

        arr.clear()
        for k in new:
            for l in k:
                if l:
                    arr.append(l)
                else:
                    break
        new = [[] for _ in range(10)]


arr = [12, 31, 24, 14, 24, 1, 4, 125, 1, 51, 25, 313, 1, 5, 1, 7, 71, 7, 17, 37, 274273]
radixSort(arr)
print(arr)