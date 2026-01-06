h, m = map(int, input().split())

m -= 45

if m < 0:
    if h == 0:
        h = 24
    h -= 1
    m += 60
    print(h, m)
else:
    if h == 24:
        h = 0
    print(h, m)