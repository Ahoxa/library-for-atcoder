# itertoolsを使う場合
from itertools import accumulate
A = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
S = list(accumulate(A))
S.insert(0, 0) # 先頭に0を挿入しておくと都合がよいことが多い

# 普通にやる場合
N = len(A)
S = [0] * (N + 1)
for i in range(N):
	S[i+1] = S[i] + A[i]

print(S)
# [0, 3, 7, 13, 15, 16, 25, 25, 32, 37, 45]