import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

dfs_visited=[]
def DFS(graph, v, visited):
    visited[v] = True
    dfs_visited.append(v)
    for i in graph[v]:
        if not visited[i]:
            DFS(graph, i, visited)

visited = [False] * (n+1)
DFS(graph, 1, visited)

print(len(dfs_visited)-1)