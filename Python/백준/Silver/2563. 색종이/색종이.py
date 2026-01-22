paper = [[0]*100 for _ in range(100)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    for y in range(b, b+10):
        for x in range(a, a+10):
            paper[y][x] = 1

area = sum(sum(row) for row in paper)
print(area)