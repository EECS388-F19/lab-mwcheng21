students = ["Jacob", "Devin", "Micah"]
students.sort()
first_name = students[0]
first_name = first_name[:-1]
print(first_name)

biggest = len(students)
biggestName = students[0]
for kids in students:
    if len(kids) > biggest:
        biggestName = kids
        biggest = len(kids)
print(biggestName)
