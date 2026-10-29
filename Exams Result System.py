GRADE_SCALE = ((80, "A"), (70, "B"), (60, "C"), (50, "D"), (0, "F"))


class Student:
    total_students = 0

    def __init__(self, student_id, name, programme):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        Student.total_students += 1

    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Programme: {self.programme}")

    @classmethod
    def from_string(cls, text):
        student_id, name, programme = text.split(",")
        return cls(student_id.strip(), name.strip(), programme.strip())

    @classmethod
    def get_total_students(cls):
        return cls.total_students


class Exam:
    def __init__(self, exam_id, course_code, title, total_marks):
        self.exam_id = exam_id
        self.course_code = course_code
        self.title = title
        self.total_marks = total_marks

    def display_info(self):
        print(f"ID: {self.exam_id} | {self.course_code} - {self.title} | Total marks: {self.total_marks}")

    @staticmethod
    def is_valid_score(score, total_marks):
        return 0 <= score <= total_marks


class Result:
    def __init__(self, student, exam, score):
        self.student = student
        self.exam = exam
        self.score = score

    def get_percentage(self):
        return self.score / self.exam.total_marks * 100

    def get_grade(self):
        percentage = self.get_percentage()
        for minimum, grade in GRADE_SCALE:
            if percentage >= minimum:
                return grade

    def update_score(self, new_score):
        if Exam.is_valid_score(new_score, self.exam.total_marks):
            self.score = new_score
            print("Score updated.")
        else:
            print("Invalid score.")

    def display_info(self):
        print(f"{self.student.name} | {self.exam.course_code} | {self.score}/{self.exam.total_marks} | "
              f"{self.get_percentage():.1f}% | Grade {self.get_grade()}")


students = {}
exams = {}
results = {}


def add_student(student):
    if student.student_id in students:
        print("Student ID already exists.")
    else:
        students[student.student_id] = student
        print("Student added.")


def add_exam(exam):
    if exam.exam_id in exams:
        print("Exam ID already exists.")
    else:
        exams[exam.exam_id] = exam
        print("Exam added.")


def add_result(student_id, exam_id, score):
    if student_id not in students:
        print("Student not found.")
    elif exam_id not in exams:
        print("Exam not found.")
    elif not Exam.is_valid_score(score, exams[exam_id].total_marks):
        print("Invalid score.")
    elif (student_id, exam_id) in results:
        print("Result already exists. Use update instead.")
    else:
        results[(student_id, exam_id)] = Result(students[student_id], exams[exam_id], score)
        print("Result added.")


def update_result(student_id, exam_id, new_score):
    key = (student_id, exam_id)
    if key in results:
        results[key].update_score(new_score)
    else:
        print("Result not found.")


def display_students():
    print("\nStudents")
    for student in students.values():
        student.display_info()
    print("Total students:", Student.get_total_students())


def display_exams():
    print("\nExams")
    for exam in exams.values():
        exam.display_info()


def display_results():
    print("\nResults")
    for result in results.values():
        result.display_info()


def display_student_results(student_id):
    print("\nResults for", student_id)
    for (sid, eid), result in results.items():
        if sid == student_id:
            result.display_info()


def read_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a number.")


def main():
    add_student(Student("S001", "Aminata", "Software Engineering"))
    add_student(Student.from_string("S002, Ibrahim, Software Engineering"))
    add_exam(Exam("E001", "PROG211", "Object-Oriented Programming 1", 100))
    add_result("S001", "E001", 85)
    add_result("S002", "E001", 62)

    while True:
        print("\n1. Add student")
        print("2. Add exam")
        print("3. Add result")
        print("4. Update result")
        print("5. Display students")
        print("6. Display exams")
        print("7. Display all results")
        print("8. Display one student's results")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(Student(input("Student ID: ").strip(), input("Name: ").strip(), input("Programme: ").strip()))
        elif choice == "2":
            add_exam(Exam(input("Exam ID: ").strip(), input("Course code: ").strip(),
                          input("Title: ").strip(), read_number("Total marks: ")))
        elif choice == "3":
            add_result(input("Student ID: ").strip(), input("Exam ID: ").strip(), read_number("Score: "))
        elif choice == "4":
            update_result(input("Student ID: ").strip(), input("Exam ID: ").strip(), read_number("New score: "))
        elif choice == "5":
            display_students()
        elif choice == "6":
            display_exams()
        elif choice == "7":
            display_results()
        elif choice == "8":
            display_student_results(input("Student ID: ").strip())
        elif choice == "0":
            break
        else:
            print("Invalid option.")


main()