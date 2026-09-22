students = ['A', 'B', 'C']

def student(x):
    return x in students

print('Student(A):', student('A'))

all_students = all(student(x) for x in students)
print("All Students:", all_students)

one_student = any(student(x) for x in students)
print("At least one student:", one_student)
