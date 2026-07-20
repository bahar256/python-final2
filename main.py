from student import Student
from course import Course
from quiz import Quiz
from exam import Exam
from project import Project
from gradebook import Gradebook

def main():
    gradebook = Gradebook()
    students_db = {}
    courses_db = {}

    # Interactive console loop
    while True:
        print("\n" + "="*30)
        print("   SCHOOL MANAGEMENT SYSTEM")
        print("="*30)
        print("1. Register New Student")
        print("2. Create New Course")
        print("3. Enroll Student in Course")
        print("4. Add Assessment to Course")
        print("5. Record Student Grade")
        print("6. Print Student Report Card")
        print("7. Exit")
        print("-"*30)
        
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            sid = input("Enter Student ID (e.g., S001): ").strip()
            if sid in students_db:
                print("Error: Student ID already exists!")
                continue
            name = input("Enter Student Name: ").strip()
            email = input("Enter Student Email: ").strip()
            students_db[sid] = Student(sid, name, email)
            print(f"Student '{name}' registered successfully.")

        elif choice == "2":
            code = input("Enter Course Code (e.g., PY101): ").strip()
            if code in courses_db:
                print("Error: Course Code already exists!")
                continue
            title = input("Enter Course Title: ").strip()
            courses_db[code] = Course(code, title)
            print(f"Course '{title}' created successfully.")

        elif choice == "3":
            sid = input("Enter Student ID: ").strip()
            code = input("Enter Course Code: ").strip()
            if sid in students_db and code in courses_db:
                courses_db[code].add_student(sid)
                print(f"Student '{students_db[sid].name}' enrolled in '{courses_db[code].course_name}'.")
            else:
                print("Error: Student ID or Course Code not found!")

        elif choice == "4":
            code = input("Enter Course Code: ").strip()
            if code not in courses_db:
                print("Error: Course not found!")
                continue
            
            print("Select Assessment Type:")
            print("1. Quiz")
            print("2. Exam")
            print("3. Project")
            type_choice = input("Enter choice (1-3): ").strip()
            
            title = input("Enter Assessment Title (e.g., Quiz 1): ").strip()
            max_score = float(input("Enter Maximum Score: "))
            
            if type_choice == "1":
                assessment = Quiz(title, max_score)
            elif type_choice == "2":
                assessment = Exam(title, max_score)
            elif type_choice == "3":
                assessment = Project(title, max_score)
            else:
                print("Invalid type choice!")
                continue
                
            courses_db[code].add_assessment(assessment)
            print(f"'{title}' added successfully to '{courses_db[code].course_name}'.")

        elif choice == "5":
            sid = input("Enter Student ID: ").strip()
            code = input("Enter Course Code: ").strip()
            if sid not in students_db or code not in courses_db:
                print("Error: Student or Course not found!")
                continue
                
            if sid not in courses_db[code].students:
                print("Error: This student is not enrolled in this course!")
                continue
                
            ass_title = input("Enter Assessment Title: ").strip()
            assessment = courses_db[code].find_assessment(ass_title)
            
            if assessment:
                score = float(input(f"Enter Score (out of {assessment.max_score}): "))
                if score > assessment.max_score:
                    print("Error: Score cannot exceed the maximum score!")
                else:
                    gradebook.add_grade(sid, assessment.title, score)
            else:
                print("Error: Assessment not found in this course!")

        elif choice == "6":
            sid = input("Enter Student ID: ").strip()
            code = input("Enter Course Code: ").strip()
            if sid in students_db and code in courses_db:
                gradebook.generate_report(students_db[sid], courses_db[code])
            else:
                print("Error: Student or Course not found!")

        

        elif choice == "7":
            print("Exiting system. Have a great day!")
            break
        else:
            print("Invalid option! Please enter a number between 1 and 7.")

if __name__== "__main__":
    main()