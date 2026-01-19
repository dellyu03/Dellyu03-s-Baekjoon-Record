N = int(input())
count = N
for _ in range(N):
    S = input()
    for i in range(0, len(S)-1):
        if S[i] == S[i+1]:
           pass
        elif S[i] in S[i+1:]:
            count -=1
            break
print(count)