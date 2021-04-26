import sys


class Deque:
    def __init__(self):
        self.arr = []

    def push_front(self, a):
        self.arr = [a] + self.arr

    def push_back(self, a):
        self.arr.append(a)

    def pop_front(self):
        if not self.arr:
            print(-1)
            return
        print(self.arr[0])
        self.arr = self.arr[1:]

    def pop_back(self):
        if not self.arr:
            print(-1)
            return
        print(self.arr.pop())

    def size(self):
        print(len(self.arr))

    def empty(self):
        if not self.arr:
            print(1)
            return
        print(0)

    def front(self):
        if not self.arr:
            print(-1)
            return
        print(self.arr[0])

    def back(self):
        if not self.arr:
            print(-1)
            return
        print(self.arr[len(self.arr) - 1])


def getInput():
    IC = int(sys.stdin.readline())
    arr = []
    for _ in range(IC):
        strs = sys.stdin.readline().strip()
        try:
            a, b = map(str, strs.split())
            arr.append([a, int(b)])
        except:
            arr.append([strs])
    return IC, arr


def solution():
    IC, arr = getInput()
    deque = Deque()
    for i in arr:
        if i[0] == "push_front":
            deque.push_front(i[1])
        if i[0] == "push_back":
            deque.push_back(i[1])
        if i[0] == "pop_front":
            deque.pop_front()
        if i[0] == "pop_back":
            deque.pop_back()
        if i[0] == "size":
            deque.size()
        if i[0] == "empty":
            deque.empty()
        if i[0] == "front":
            deque.front()
        if i[0] == "back":
            deque.back()


solution()
