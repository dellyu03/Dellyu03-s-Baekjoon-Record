T = int(input())

for i in range(T):
    answer = ""
    R, S = input().split()
    R = int(R)
    for _ in range(len(S)):
        answer += S[_]*R
        
    print(answer)