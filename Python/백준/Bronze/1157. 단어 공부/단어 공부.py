S = input()

S = S.upper()

count = []

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for _ in alphabet:
    a = S.count(_)
    count.append(a)

if count.count(max(count)) >1:
    print("?")
else:
    print(alphabet[count.index(max(count))])