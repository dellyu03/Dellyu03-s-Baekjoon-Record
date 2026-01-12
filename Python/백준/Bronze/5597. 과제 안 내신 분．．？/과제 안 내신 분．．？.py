students = [i for i in range(1,31)]

for i in range(28):
    present = int(input())
    students.remove(present)

students.sort()
print(str(students[0]) + " " + str(students[1]))