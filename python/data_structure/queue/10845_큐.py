import sys


class Queue:
    def __init__(self):
        self.arr = []

    def push(self, a):
        self.arr.append(a)

    def pop(self):
        if len(self.arr) == 0:
            print(-1)
        else:
            print(self.arr[0])
            self.arr = self.arr[1:]

    def size(self):
        print(len(self.arr))

    def empty(self):
        if self.arr:
            print(0)
        else:
            print(1)

    def front(self):
        if self.arr:
            print(self.arr[0])
        else:
            print(-1)

    def back(self):
        if self.arr:
            print(self.arr[len(self.arr) - 1])
        else:
            print(-1)


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
    queue = Queue()
    IC, arr = getInput()
    for i in arr:
        if i[0] == "push":
            queue.push(i[1])
        elif i[0] == "pop":
            queue.pop()
        elif i[0] == "size":
            queue.size()
        elif i[0] == "empty":
            queue.empty()
        elif i[0] == "front":
            queue.front()
        elif i[0] == "back":
            queue.back()


solution()