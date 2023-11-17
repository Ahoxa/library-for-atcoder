import sys

sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# スタートとゴールの位置を全探索で調べる
start, goal = None, None
for i in range(H):
    for j in range(W):
        if maze[i][j] == "s":
            start = (i, j)
        elif maze[i][j] == "g":
            goal = (i, j)

        if start and goal:
            break

    if start and goal:
        break

# 上下左右
dh = [1, -1, 0, 0]
dw = [0, 0, -1, 1]

# 訪問チェックリスト
visited = [[False] * W for _ in range(H)]


def dfs(now_h, now_w):
    visited[now_h][now_w] = True

    for i in range(4):
        next_h = now_h + dh[i]
        next_w = now_w + dw[i]

        # 場内に収まっているか
        if 0 <= next_h < H and 0 <= next_w < W:
            # 壁ではないか
            if maze[next_h][next_w] != "#":
                # 訪問済みではないか(未訪問か)
                if visited[next_h][next_w] == False:
                    dfs(next_h, next_w) # 再起関数はPyPyだと遅いことに注意


dfs(start[0], start[1])

print("Yes" if visited[goal[0]][goal[1]] else "No")
