
n = int(input())

for i in range(n):
    star = "*" * (i+1)
    print("{:>{width}}".format(star, width = n))