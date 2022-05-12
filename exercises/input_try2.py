names = input("c, p, m, r: ").title().split(",")
assignments = input("3, 6, 0, 2: ").split(",")
grades = input("81, 77, 92, 88: ").split(",")

for name in range("names"):

    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in names, assignments, grades:
    print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))
