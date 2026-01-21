import sys

table = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

max_num = -1
max_row = 0
max_col = 0

for r in range(9):
    for c in range(9):
        if table[r][c] > max_num:
            max_num = table[r][c]
            max_row = r
            max_col = c

print(max_num)
print(max_row + 1, max_col + 1)

