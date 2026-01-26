import sys

T = int(input())

coins = [25, 10, 5, 1]


for _ in range(T):
    count = [0, 0, 0, 0]
    c = int(sys.stdin.readline().strip())
    i = 0
    while c != 0:
        count[i] = c // coins[i]
        c = c % coins[i]
        i += 1
    for j in range(4):
        print(count[j], end=' ')


        