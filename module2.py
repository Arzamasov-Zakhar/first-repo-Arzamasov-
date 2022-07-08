import module1
class Student_with_additional_inf(module1.Student):
    def __init__(self, name, age = "", gender = "", status=""):
        self.name = name
        self.age = age
        self.gender = gender
        self.status = status
        
    def input_gender(self,gender):
        self.gender = gender
        
        
    def input_status(self, status):    
        self.status = status
        
        
    def print_gender(self):
        print(f"Пол студента {self.name}: {self.gender}")
        
        
    def print_status(self):    
        print(f"Семейное положение студента {self.name}: {self.status}")    
        
        
   
