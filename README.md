# Mohamed-Sheriff-Kabia_905006315_DIT1102_Assignment1-Exam-Result-Management-System
# Digital Exam & Results Management System

**Module:** PROG211 Object-Oriented Programming 1
**Assignment:** Real-World Solutions under DPG Standards
**Domain:** Education

## About the project

This is a simple Python program that helps a school or university keep track of exams and student results. In many places, exam results are still written in books or on loose sheets, which makes them easy to lose, hard to check and slow to calculate. This program lets a lecturer or exam officer do the following:

- Add students
- Add exams
- Record a student's score for an exam
- Update a score if a mistake was made
- View students, exams and results
- See the percentage and grade of each result automatically

The program runs in the terminal and uses object-oriented programming (OOP).

## How to run it

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

```
python exam_results_system.py
```

## Files in this repository

| File | Description |
|---|---|
| `exam_results_system.py` | The Python source code |
| `README.md` | This file |

## How the program is built

### Classes and objects

| Class | What it is used for |
|---|---|
| `Student` | Stores a student's ID, name and programme |
| `Exam` | Stores the exam ID, course code, title and total marks |
| `Result` | Links one `Student` object to one `Exam` object and stores the score |

The `Result` class shows how objects work together, because every result holds a student object and an exam object.

### Data structure

The program uses **dictionaries** to store the objects:

- `students` stores each student using the student ID as the key
- `exams` stores each exam using the exam ID as the key
- `results` stores each result using the student ID and exam ID together as the key

The functions `add_student()`, `add_exam()` and `add_result()` add records to the dictionaries. The functions `display_students()`, `display_exams()` and `display_results()` loop through them and show the records.

I also used **tuples** in two places: the `GRADE_SCALE` (the grade boundaries) and the `(student_id, exam_id)` keys of the results dictionary.

### Methods

| Type | Methods |
|---|---|
| Instance methods | `display_info()`, `get_percentage()`, `get_grade()`, `update_score()` |
| Class methods (`@classmethod`) | `Student.from_string()`, `Student.get_total_students()` |
| Static method (`@staticmethod`) | `Exam.is_valid_score()` |

## How it supports Digital Public Goods (DPG) standards

**1. Open-source**
The full source code is uploaded to GitHub in a public repository, so anyone can read it, use it, copy it and improve it for free.

**2. Inclusive and accessible design**
The program uses a simple numbered menu and short, clear messages. It does not need a fast computer, internet or any paid software, only Python, so schools with limited resources can still use it. It also tells the user when something is wrong (for example "Invalid score" or "Student not found") instead of crashing.

**3. Privacy-respecting (no sensitive personal data)**
The program only stores a student ID, a name and a programme. It does not store phone numbers, addresses, dates of birth, photos, ID card numbers or any other sensitive information. Schools can use a student ID or a nickname instead of a full name, which keeps the students' identity protected.

**4. Modular and reusable**
Each class has one job. `Student` handles student details, `Exam` handles exam details and `Result` handles scores and grades. The functions for adding and displaying records are also separate. This means any part can be changed or reused in another project, for example, the grade scale can be changed in one place (`GRADE_SCALE`) without touching the rest of the code.

## Example usage

Below is a sample run of the program. The program starts with two students (Aminata and Ibrahim), one exam (PROG211) and two results already added. In this run, a new student and a new exam are added, then a result is recorded, and then an invalid score is tried.

**Sample input and output**

```
Choose an option: 1
Student ID: S003
Name: Fatmata
Programme: Networking
Student added.

Choose an option: 2
Exam ID: E002
Course code: DBMS201
Title: Database Management
Total marks: 50
Exam added.

Choose an option: 3
Student ID: S003
Exam ID: E002
Score: 41
Result added.

Choose an option: 3
Student ID: S003
Exam ID: E001
Score: 150
Invalid score.

Choose an option: 7

Results
Aminata | PROG211 | 85/100 | 85.0% | Grade A
Ibrahim | PROG211 | 62/100 | 62.0% | Grade C
Fatmata | DBMS201 | 41.0/50.0 | 82.0% | Grade A

Choose an option: 8
Student ID: S001

Results for S001
Aminata | PROG211 | 85/100 | 85.0% | Grade A
```

## Grading scale

| Percentage | Grade |
|---|---|
| 80 and above | A |
| 70 to 79 | B |
| 60 to 69 | C |
| 50 to 59 | D |
| Below 50 | F |

## Author

Muhammad
Limkokwing University of Creative Technology, Sierra Leone
