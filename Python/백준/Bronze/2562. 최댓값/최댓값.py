import sys
li = sys.stdin.readlines()
li = list(map(int, li))

m = max(li)
print(m)
print(li.index(m)+1)