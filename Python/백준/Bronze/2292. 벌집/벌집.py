n = int(input())
s = 1
count = 1
while s < n:
    s += 6*count
    count += 1
print(count)