import sys

sys.setrecursionlimit(10**7)
def DFS(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

count = 0
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        DFS(graph, i, visited)
        count += 1

print(count)