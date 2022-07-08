class Student():
    
    def __init__(self, name):
        self.name = name
    
        
        
        
    def input_name(self,name):
        self.name = name
        
        
    def input_age(self, age):    
        self.age = int(age)
        
        
    def print_name(self):
        print("Имя студента:", self.name)
        
        
    def print_age(self):    
        print(f"Возраст студента {self.name}: {self.age}")
        
 
