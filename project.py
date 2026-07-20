from assessment import Assessment

class Project(Assessment):
    def display_info(self):
        print(f"project : {self.title } max score :{self.max_score}")
    
    def grade_messege(self, score):
        percentage = self.calculate_percentage(score)
         
        if percentage >= 90 :
            return "you are the best!"
        elif percentage >= 55 :
            return "work harder"
        else :
            return "project needs improvment ."