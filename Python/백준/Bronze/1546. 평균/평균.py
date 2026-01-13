import sys
n = int(input())

scores = []
scores = list(map(int, sys.stdin.readline().strip().split()))
m = max(scores)
sum = 0
for i in range(n):
        scores[i] = scores[i] / m*100
        sum += scores[i]
    
print(sum/n)