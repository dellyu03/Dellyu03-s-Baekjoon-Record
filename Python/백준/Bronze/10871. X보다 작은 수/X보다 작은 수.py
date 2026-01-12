n, x = map(int, input().split())
a = input().split()
answer = []

for i in a:
    i=int(i)
    if i < x:
        answer.append(i)
        
for i in answer:
    print(i, sep =" ")