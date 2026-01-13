numbers = int(input())
scores = list(map(int, input().split()))
M = max(scores)
sum = 0

for i in range(numbers):
    nScore = scores[i]/M*100
    sum += nScore
    
print(sum/numbers)

    