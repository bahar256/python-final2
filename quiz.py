#importing the parent class
from assessment import Assessment

class Quiz(Assessment):
    def display_info(self):
        print(f"Quiz : {self.title}  max score :{self.max_score}")

    def grade_messege(self, score):
        percentage = self.calculate_percentage (score)     #using the parent class 
        if percentage >= 80:
            return "great job, you did well!!"
        return "keep practicing and work harder."
            