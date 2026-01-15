correct = [1, 1, 2, 2, 2, 8]

found = list(map(int, input().split()))

to_do = []

for i in range(len(correct)):
    a = correct[i] - found[i]
    to_do.append(a)
print(*to_do, end=' ')