class Student():

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def input_name(self, name):
        self.name = name

    def input_age(self, age):
        self.age = age

    def print_name(self):
        print('Имя студента:', self.name)

    def print_age(self):
        print(f'Возраст студента {self.name}: {self.age}')
