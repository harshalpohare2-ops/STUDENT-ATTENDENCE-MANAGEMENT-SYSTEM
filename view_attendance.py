# Function 3: View Attendance

from data import students


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
