# Student Marks Dictionary
# Write a Python program to take a student name and marks as input and store them in a dictionary.
# Display the student name and marks.

record = {}
i = int(input("Enter the size you want add the record "))

for j in range(i):
    name = input("Enter your name: ")
    marks = input("Enter your marks: ")
    record[name] = marks;

for name, marks in record.items():
    print("Student Name:", name)
    print("Marks:", marks)