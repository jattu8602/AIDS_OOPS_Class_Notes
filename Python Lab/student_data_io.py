# Collecting student's basic details
name = input("Enter student's name: ")
age = input("Enter student's age: ")
roll_number = input("Enter student's roll number: ")
course = input("Enter student's course: ")

# Collecting student's marks for 3 subjects
marks = {}
for i in range(1, 4):
    subject = input(f"Enter the name of subject {i}: ")
    subject_marks = input(f"Enter the marks for {subject}: ")
    marks[subject] = subject_marks

# Printing student details
print("\nStudent Details:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Roll Number: {roll_number}")
print(f"Course: {course}")

# Printing student marks
print("\nMarks:")
for subject, subject_marks in marks.items():
    print(f"{subject}: {subject_marks}")
