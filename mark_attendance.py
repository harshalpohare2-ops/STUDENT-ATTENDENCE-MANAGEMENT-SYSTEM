# Function 2: Mark Attendance

from data import students


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
