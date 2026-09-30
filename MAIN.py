# Student Attendance Management System

students = {}


# Function 1: Add Student
def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    students[roll_no] = {
        "name": name,
        "present": 0,
        "total": 0
    }

    print("Student added successfully!")


# Function 2: Mark Attendance
def mark_attendance():
    if len(students) == 0:
        print("No students available.")
    else:
        for roll_no in students:
            name = students[roll_no]["name"]

            attendance = input(
                f"Is {name} present? (P/A): "
            ).upper()

            students[roll_no]["total"] += 1

            if attendance == "P":
                students[roll_no]["present"] += 1

        print("Attendance marked successfully!")


# Function 3: View Attendance
def view_attendance():
    if len(students) == 0:
        print("No students available.")
    else:
        print("\n===== ATTENDANCE REPORT =====")

        for roll_no in students:
            name = students[roll_no]["name"]
            present = students[roll_no]["present"]
            total = students[roll_no]["total"]

            if total > 0:
                percentage = (present / total) * 100
            else:
                percentage = 0

            print("\nRoll No:", roll_no)
            print("Name:", name)
            print("Present:", present)
            print("Total Classes:", total)
            print("Attendance:", percentage, "%")


# Main Program
while True:
    print("\n===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        mark_attendance()

    elif choice == 3:
        view_attendance()

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")