class Gradebook :
    def __init__(self):
        self.grades = {}
    
    def add_grade (self, student_id, assessment_title , score):
        if student_id not in self.grades:
            self.grades[student_id] = {}

        self.grades[student_id][assessment_title] = score 
        print(f"grade ; {score} added for student {student_id} in {assessment_title}.")
    
    def get_grade (self, student_id , assessment_title ,score):
        if student_id  not in self.grades and assessment_title in self.grades[student_id]:
            return self.grades[student_id][assessment_title]
        return None
    
    def calculate_gpa (self , student_id , course):   #for calculating the percentages of students 
        if student_id not in self.grades or not course.assessments:
            return 0.0 
        total_percentage = 0
        count = 0 

        for assessment in course.assessments: #going through every student in class 
            if assessment.title in self.grades[student_id]:
               score = self.grades[student_id][assessment.title]
               percentage = assessment.calculate_percentage(score) #changing numbers to percentages
               total_percentage += percentage
               count +=1

            return total_percentage / count if count > 0 else 0.0 
        
    def generate_report(self , student , course):
        student_id = student.get_id()
        print(f"report card : {course.course_name}")
        print(f"student name : {student.name}")
        print(f"student id : {student_id}")

        if student_id not in self.grades :
            print("there is no grade for this student .")

        for assessment in course.assessments:
            if assessment.title in self.grades[student_id]:
                score = self.grades[student_id][assessment.title]
                percentage = assessment.calculate_percentage(score)

                messege = assessment.grade_messege(score)

                print(f" {assessment.title } : {score}/{assessment.max_score} ({percentage : .1f}%) {messege} ")
                 
            else :
                print(f"{assessment.title}: not taken ")
            
        gpa = self.calculate_gpa(student_id , course)
        print(f"final score : {gpa: .1f}%")