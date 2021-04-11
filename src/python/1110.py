def solution():
    I = int(input())
    count = 0
    first = I // 10
    last = I % 10
    while 1:
        if I == (first * 10 + last) and count != 0:
            break
        temp = first
        first = last
        last = (temp + last) % 10
        count += 1
    print(count)


solution()
