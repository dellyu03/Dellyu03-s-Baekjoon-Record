import sys

result = 0
subjects = 20
hakjeom = 0.0

for _ in range(20):
    s = list(sys.stdin.readline().strip().split())
    if s[2] == "P":
        subjects += -1
        continue
    else:
        if s[2] == "A+":
            score = 4.5
        if s[2] == "A0":
            score = 4.0
        if s[2] == "B+":
            score = 3.5
        if s[2] == "B0":
            score = 3.0
        if s[2] == "C+":
            score = 2.5
        if s[2] == "C0":
            score = 2.0
        if s[2] == "D+":
            score = 1.5
        if s[2] == "D0":
            score = 1.0
        if s[2] == "F":
            score = 0.0
        sub_score = score * float(s[1])
        result += sub_score
        hakjeom += float(s[1])
result = result / hakjeom
print(result)