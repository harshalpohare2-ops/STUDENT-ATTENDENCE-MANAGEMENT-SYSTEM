# Problem Statement

## Title
Student Attendance Management System

## Problem
In many classrooms, attendance is still recorded on paper registers. Calculating each student's attendance percentage by hand at the end of a term is slow and error-prone, and it is hard to quickly see how regular a student has been.

## Objective
To build a simple, easy-to-use Python program that records student attendance and automatically calculates attendance percentages, replacing manual register-keeping.

## Scope
The system will:

1. Store student records (roll number and name).
2. Record attendance (present or absent) for every student in each class.
3. Keep a running count of classes attended and total classes held.
4. Display a report showing each student's attendance percentage.

The current version runs in the command line and keeps data in memory for a single session.

## Target Users
- Teachers and faculty who take class attendance
- Students or small institutions needing a lightweight attendance tool

## Functional Requirements

| ID | Requirement |
|----|-------------|
| FR1 | The user shall be able to add a student with a roll number and name. |
| FR2 | The user shall be able to mark each student present or absent for a class. |
| FR3 | The system shall calculate attendance percentage as (present ÷ total classes) × 100. |
| FR4 | The user shall be able to view an attendance report for all students. |
| FR5 | The system shall show a clear message when no students exist or a menu choice is invalid. |

## Non-Functional Requirements
- **Simplicity:** menu-driven interface that needs no training.
- **Portability:** runs on any system with Python 3 and no external libraries.
- **Readability:** modular functions with clear names and comments.

## Expected Outcome
A working console application that lets a teacher add students, mark attendance, and instantly view accurate attendance percentages.
