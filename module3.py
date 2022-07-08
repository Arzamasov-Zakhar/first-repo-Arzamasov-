import pickle
from module2 import Student_with_additional_inf
        
class Container():
    def __init__(self, group=None):
        if group is None:
            self.group = []
        else:
            self.group = group
        
    
    def group_append(self, elem):
        self.group.append(elem)
        
    
    def group_print(self):
        print(*self.group, sep=", ", end=".\n")
        
     
    def group_read_file(self, file_name):
        with open (file_name, "rb") as file:
            load_list = pickle.load(file)            
            self.group = load_list
            list_group1 = []
            for i in load_list:
                list_group1.append(Student_with_additional_inf(i))
    

    def group_write_file(self, file_name):
        with open (file_name, "wb") as file:
            pickle.dump(self.group, file)
            

    def group_clear(self):
        self.group = []
          
