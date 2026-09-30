# Student Attendance Management System

A simple command-line application written in Python that lets a teacher add students, mark daily attendance, and view each student's attendance percentage.

## Features

- **Add Student** – register a student with a roll number and name.
- **Mark Attendance** – go through every student and mark Present (`P`) or Absent (`A`) for a class.
- **View Attendance** – see present count, total classes and attendance percentage for every student.
- **Menu-driven interface** – runs in a loop until the user chooses Exit.
- **Input handling** – shows friendly messages for an empty student list or an invalid menu choice.

## Requirements

- Python 3.8 or higher
- No external libraries (uses only built-in Python)

## How to Run

```bash
python MAIN.py
```

## Usage

When the program starts, the following menu is shown:

```
===== STUDENT ATTENDANCE MANAGEMENT SYSTEM =====
1. Add Student
2. Mark Attendance
3. View Attendance
4. Exit
```

| Option | What it does |
|--------|--------------|
| 1 | Asks for roll number and name, then stores the student |
| 2 | Asks `Is <name> present? (P/A)` for each student and updates counts |
| 3 | Prints a report of present days, total classes and percentage |
| 4 | Exits the program |

### Sample Output

```
===== ATTENDANCE REPORT =====

Roll No: 101
Name: Aarav Sharma
Present: 2
Total Classes: 2
Attendance: 100.0 %

Roll No: 102
Name: Priya Verma
Present: 1
Total Classes: 2
Attendance: 50.0 %
```

More screenshots are available in the `screenshots/` folder.

## How It Works

Student data is kept in a Python dictionary, keyed by roll number:

```python
students = {
    101: {"name": "Aarav Sharma", "present": 2, "total": 2}
}
```

Attendance percentage is calculated as:

```
percentage = (present / total) * 100
```

## Project Structure

```
.
├── MAIN.py          # Application source code
├── README.md        # Project documentation
├── statement.md     # Problem statement
└── screenshots/     # Program output screenshots
    ├── 01_menu_and_empty.png
    ├── 02_add_students.png
    ├── 03_mark_attendance.png
    └── 04_view_report.png
```

## Limitations

- Data is stored in memory only and is lost when the program exits.
- Adding a student with an existing roll number overwrites the old record.
- Entering a non-numeric roll number or menu choice stops the program with an error.
- Any entry other than `P` is counted as absent.

## Future Improvements

- Save and load data using a file (CSV/JSON) or database
- Validate all inputs and prevent duplicate roll numbers
- Add options to edit or delete students
- Highlight students below 75% attendance
- Track attendance by date and subject
