# School Management & Gradebook System

A modular Python-based Command Line Interface (CLI) application developed using Object-Oriented Programming (OOP) principles. This system manages student enrollments, course creations, weighted assessment structures, grade calculations, and automated report card generation.

---

## 📌 Project Architecture & Features

The system is designed with a clear separation of concerns, dividing data models, computation logic, and user interaction into distinct modules.

### Core Features
* Student Registration: Add and maintain student records using unique identifiers.
* Course Creation: Define course details including course codes and titles.
* Enrollment Management: Link registered students directly to specific available courses.
* Flexible Assessment Weighting: Assign customized weighted assessments (such as Quizzes, Midterms, Final Exams, and Projects) to individual courses.
* Automated Grade Calculation: Input student performance per assessment and automatically calculate weighted totals and grade percentages.
* Report Card Generation: Produce a structured summary displaying course performance, scores, and grade point averages (GPA).

---

## 🏗️ File Structure & Code Overview

### 1. course.py
This module defines the Course class, which serves as the data structure for individual academic courses.
* __init__(self, course_code, course_name): Initializes the course object with its code (e.g., CS101) and name.
* __str__(self): Overrides the string representation to display course details in a human-readable format.

### 2. assessment.py
This module defines the Assessment class, which handles assessment components and weight distrinit__init__(self, name, weight): Defines the assessment type (e.g., "Final Exam") and its percentage weight towards the final grade (e.g., 0.5 for 50%).
* assign_grade(self, score): Validates and assigns a raw numerical score to the assessment.
* get_weighted_score(self): Multiplies the raw score by the assessment weight to determine its actual contribution to the overall course grade.

### 3. gradebook.py
This module contains the GradeBook class, which acts as the core controller and database manager for the system.
* students_db / courses_db: Internal dictionary structures that store registered students, enrolled courses, and grade mapping.
* register_student(student_id, name): Adds a new student record to the system.
* create_course(course_code, course_name): Adds a new course entry to the system.
* enroll_student(student_id, course_code): Establishes a link between a student and a course.
* record_grade(student_id, course_code, assessment_name, score): Stores an assessment score for a specific enrolled student after verifying record validity.
* calculate_gpa(student_id, course_code): Aggregates all weighted assessment scores to compute the final course percentage and grade point equivalent.
* generate_report(student_id, course_code): Formats and prints a detailed academic report card for a student in the terminal.

### 4. main.py
This is the entry point of the application, implementing an interactive CLI.
* Imports classes from course.py, assessment.py, and gradebook.py.
* Uses a while loop to present an interactive menu (Options 1–8) to the user.
* Processes user selections using conditional statements (if/elif/else) and invokes corresponding methods from the GradeBook instance
