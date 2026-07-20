#making the class 
class Student :
    def __init__(self, student_id,name, email):
        self.__student_id = student_id    # using Encapsulation
        self.name = name
        self.email = email
        self.course = []  #making a empty list so that the courses a student  can be added here

    def get_id(self):
        return self.__student_id #using getter  
    def set_email(self , new_email):
        if "@" in new_email and "." in new_email:
            self.email = new_email
            return True 
        return False
