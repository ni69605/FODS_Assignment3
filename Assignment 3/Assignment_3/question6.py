'''This program creates a class student info.'''
class Student:
    def _init_(self):
        self.id = input("ID: ")
        self.name = input("Name: ")
        self.address = input("Address: ")
        self.year = input("Admission Year: ")
        self.level = input("Level: ")
        self.section = input("Section: ")

    def display(self):
        print("\nStudent Details:")
        for attr, value in vars(self).items():
            print(f"{attr}: {value}")

s = Student()
s.display()