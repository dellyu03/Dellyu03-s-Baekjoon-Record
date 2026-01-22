import sys

S = [line.rstrip('\n') for line in sys.stdin.readlines()]  

max_len = max(len(line) for line in S)

for j in range(max_len):
    for i in range(5):
        if j < len(S[i]):         
            print(S[i][j], end="")