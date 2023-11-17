from collections import deque

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

que = deque()
visited = [[False] * W for _ in range(H)]
dh = [1, -1, 0, 0]
dw = [0, 0, -1, 1]

que.append(start)
visited[start[0]][start[1]] = True
while que:
    now_h, now_w = que.popleft()
    for i in range(4):
        next_h = now_h + dh[i]
        next_w = now_w + dw[i]
        # 今回はゴール('g')も配慮しないといけないので != "#"で判定
        if 0 <= next_h < H and 0 <= next_w < W and maze[next_h][next_w] != "#":
            if visited[next_h][next_w] == False:
                visited[next_h][next_w] = True
                que.append([next_h, next_w])

print("Yes" if visited[goal[0]][goal[1]] == True else "No")

# 10 10
# s.........
# #########.
# #.......#.
# #..####.#.
# ##....#.#.
# #####.#.#.
# g.#.#.#.#.
# #.#.#.#.#.
# #.#.#.#.#.
# #.....#...
