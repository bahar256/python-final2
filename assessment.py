class Assessment :
    def __init__(self , title , max_score):
        self.title = title
        self.max_score = max_score

    def calculate_percentage(self, score):
        if self.max_score == 0 :
            return 0 
        return (score / self.max_score) * 100 
    
    def grade_messege(self , score):
        return "Assessment completed."
    
    def display_info(self):
        print(f"{self.title} (max score : {self.max_score})")
