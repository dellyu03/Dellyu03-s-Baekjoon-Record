N, M = map(int, input().split())
baskets = []
for a in range(N):
    baskets.append(0)

for b in range(M):
    i, j, k = map(int, input().split())
    for ball_index in range(i-1, j):
        baskets[ball_index] = k


for c in range(N):
    print(baskets[c], end=' ')