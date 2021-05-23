import sys


class Node:
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class Tree:
    def __init__(self, item=None):
        self.root = Node(item)

    def appendLeft(self, to, item):
        no = Node(item)
        if item != ".":
            to.left = no

    def appendRight(self, to, item):
        no = Node(item)
        if item != ".":
            to.right = no

    def find(self, fr, find):
        if fr.left == None:
            pass
        elif fr.right == None:
            pass
        elif fr.left == find:
            return fr.left
        elif fr.right == find:
            return fr.right
        else:
            self.find(fr.left, find)
            self.find(fr.left, find)


def getInput():
    IC = int(sys.stdin.readline())
    tree = Tree()
    R = 0
    for _ in range(IC):
        root, left, right = map(str, sys.stdin.readline().split())
        if tree.root.item == None:
            tree = Tree(root)
            R = tree.root
        else:
            R = tree.find(tree.root, root)
        tree.appendLeft(R, left)
        tree.appendRight(R, right)
        print(tree.root.left)


def solution():
    tree = getInput()
    pass


solution()