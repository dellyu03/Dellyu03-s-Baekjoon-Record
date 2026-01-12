lefts = []

for n in range (10):
    i = int(input())
    left = i%42
    if left not in lefts:
        lefts.append(left)
        
print(len(lefts))