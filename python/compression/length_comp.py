S = "AAAABBBBBBBBCAAADDD"

# 手動で
res = []
N = len(S)
i = 0
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    res.append((S[i], j - i))
    i = j

print(res)

# ライブラリを用いる
from itertools import groupby

ans = []
for string, group in groupby(S):
    ans.append((string, len(list(group))))

# リスト内包表記だとこう
# ans = [(string, len(list(group))) for string, group in groupby(S)]

print(ans)

# どちらも一緒
print("Yes" if res == ans else "No")
# Yes
