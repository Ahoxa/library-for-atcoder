N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

visited = [False] * N


def dfs(now):
    visited[now] = True
    for next in G[now]:
        if visited[next]:
            continue
        dfs(next)


count = 0
for now in range(N):
    if visited[now]:
        continue
    dfs(now)
    count += 1

print(count)
