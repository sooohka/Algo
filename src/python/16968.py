count = 0

def rec(strs,visited):
    for i in range(len(strs)):
        if not visited[i]:



def solution():
    strs = input()
    visited=[False]*len(strs)
    rec(strs,visited)

solution()
