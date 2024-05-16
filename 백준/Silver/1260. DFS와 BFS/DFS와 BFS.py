import sys

sys.setrecursionlimit(10**7)

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)
    graph[s].sort()
    graph[e].sort()


# dfs 구하기
dfs_visited = []
def DFS(graph, v, visited1):
    visited1[v] = True
    dfs_visited.append(v)
    for i in graph[v]:
        if not visited1[i]:
            DFS(graph, i, visited1)


# bfs 구하기
from collections import deque

bfs_visited = []
def BFS(graph, v, visited2):
    queue = deque([v])
    visited2[v] = True
    while queue:
        b = queue.popleft()
        bfs_visited.append(b)

        for i in graph[b]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True


visited1 = [False] * (n+1)
visited2 = [False] * (n+1)
DFS(graph, v, visited1)
BFS(graph, v, visited2)
print(*dfs_visited, sep=' ')
print(*bfs_visited, sep=' ')