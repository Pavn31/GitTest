# ==========================================
#          STUDENT MANAGEMENT SYSTEM
# ==========================================

import os
import json
import datetime
import random

# Application settings
APP_NAME = "Student Management System"
VERSION = "1.0"

students = []


# ==========================================
# STUDENT CLASS
# ==========================================

class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):

        print("\n-----------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())
        print("-----------------------------")


# ==========================================
# SAVE DATA
# ==========================================

def save_data():

    data = []

    for student in students:

        data.append({
            "id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        })

    try:
        with open("students.json", "w") as file:
            json.dump(data, file, indent=4)

        print("Data saved successfully!")

    except Exception as error:
        print("Error saving data:", error)


# ==========================================
# LOAD DATA
# ==========================================

def load_data():

    global students

    if not os.path.exists("students.json"):
        return

    try:
        with open("students.json", "r") as file:
            data = json.load(file)

        for item in data:

            student = Student(
                item["id"],
                item["name"],
                item["age"],
                item["course"],
                item["marks"]
            )

            students.append(student)

        print("Data loaded successfully!")

    except Exception as error:
        print("Error loading data:", error)


# ==========================================
# ADD STUDENT
# ==========================================

def add_student():

    print("\nADD NEW STUDENT")

    try:

        student_id = random.randint(1000, 9999)

        name = input("Enter student name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        marks = float(input("Enter marks: "))

        if not name.strip():
            print("Name cannot be empty!")
            return

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks!")
            return

        student = Student(
            student_id,
            name,
            age,
            course,
            marks
        )

        students.append(student)

        save_data()

        print("Student added successfully!")
        print("Student ID:", student_id)

    except ValueError:
        print("Please enter valid numbers!")


# ==========================================
# DISPLAY ALL STUDENTS
# ==========================================

def display_students():

    if len(students) == 0:
        print("No students found!")
        return

    print("\nALL STUDENTS")

    for student in students:
        student.display()


# ==========================================
# SEARCH STUDENT
# ==========================================

def search_student():

    search_id = input("Enter student ID: ")

    for student in students:

        if str(student.student_id) == search_id:

            print("Student found!")
            student.display()
            return

    print("Student not found!")


# ==========================================
# DELETE STUDENT
# ==========================================

def delete_student():

    search_id = input("Enter student ID to delete: ")

    for student in students:

        if str(student.student_id) == search_id:

            students.remove(student)

            save_data()

            print("Student deleted successfully!")
            return

    print("Student not found!")


# ==========================================
# UPDATE STUDENT
# ==========================================

def update_student():

    search_id = input("Enter student ID: ")

    for student in students:

        if str(student.student_id) == search_id:

            print("1. Update Name")
            print("2. Update Age")
            print("3. Update Course")
            print("4. Update Marks")

            choice = input("Choose option: ")

            if choice == "1":
                student.name = input("New name: ")

            elif choice == "2":
                student.age = int(input("New age: "))

            elif choice == "3":
                student.course = input("New course: ")

            elif choice == "4":
                marks = float(input("New marks: "))

                if not 0 <= marks <= 100:
                    print("Invalid marks!")
                    return

                student.marks = marks

            else:
                print("Invalid option!")
                return

            save_data()

            print("Student updated successfully!")
            return

    print("Student not found!")


# ==========================================
# STATISTICS
# ==========================================

def show_statistics():

    if not students:
        print("No student records available.")
        return

    total = len(students)

    average = sum(
        student.marks for student in students
    ) / total

    highest = max(
        students,
        key=lambda student: student.marks
    )

    lowest = min(
        students,
        key=lambda student: student.marks
    )

    print("\nSTUDENT STATISTICS")
    print("Total Students:", total)
    print("Average Marks:", round(average, 2))

    print("Highest Scorer:", highest.name)
    print("Highest Marks:", highest.marks)

    print("Lowest Scorer:", lowest.name)
    print("Lowest Marks:", lowest.marks)


# ==========================================
# MAIN MENU
# ==========================================

def main():

    load_data()

    while True:

        print("\n================================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Statistics")
        print("7. Save Data")
        print("8. Exit")

        print("================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            show_statistics()

        elif choice == "7":
            save_data()

        elif choice == "8":
            save_data()
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice! Try again.")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":
    main()
