from assessment import Assessment

class Exam(Assessment):
    def grade_messege(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 55 :
            return "yuo passed but work harder"
        return "you failed . try more "
