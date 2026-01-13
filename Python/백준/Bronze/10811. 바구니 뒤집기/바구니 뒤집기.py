N, M = map(int, input().split())
list = []

for _ in range(1, N + 1):
    list.append(_)

for _ in range(M):
    j, k = map(int, input().split())
    temp = list[j - 1: k]
    temp.reverse()
    list[j - 1:k] = temp

print(*list, end='')
    