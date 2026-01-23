N, B = input().split()

B = int(B)

result = 0
t = len(N)-1

for i in N:
    int_num = ord(i)
    if "A" <= i <="Z":
        result += (int_num - 55) * B ** t
    else:
        num = int(i)
        result += num * B **t
    t-=1

print(result)
