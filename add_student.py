# Function 1: Add Student

from data import students


def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    students[roll_no] = {
        "name": name,
        "present": 0,
        "total": 0
    }

    print("Student added successfully!")
