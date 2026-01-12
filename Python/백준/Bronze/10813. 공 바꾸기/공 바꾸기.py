N, M = map(int, input().split())

baskets = [i for i in range(1, N+1)]

for t in range(M):
    i, j = map(int, input().split())
    temp = baskets[i-1]
    baskets[i-1] = baskets[j-1]
    baskets[j-1] = temp
    
for i in baskets:
    print(i, end=" ")