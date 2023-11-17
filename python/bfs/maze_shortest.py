from collections import deque

que = deque()

# 入力受け取り
H, W = map(int, input().split())
start = list(map(int, input().split()))
goal = list(map(int, input().split()))
Maze = [list(input()) for _ in range(H)]

# 未訪問チェッカー
dist = [[-1] * W for _ in range(H)]

# 上下左右
dh = [1, -1, 0, 0]
dw = [0, 0, -1, 1]

dist[0][0] = 0

que.append(start)
while que:
    now_h, now_w = que.popleft()
    for i in range(4):
        next_h = now_h + dh[i]
        next_w = now_w + dw[i]
        if 0 <= next_h < H and 0 <= next_w < W and Maze[next_h][now_w] == ".":
            if dist[next_h][next_w] == -1:
                dist[next_h][next_w] = dist[now_h][now_w] + 1
                que.append([next_h, next_w])

print(dist[goal[1]][goal[0]])

# sample input
# 5 5
# 0 0
# 4 4
# .....
# ...#.
# ..#..
# #...#
# .....

# expected output
# 8
