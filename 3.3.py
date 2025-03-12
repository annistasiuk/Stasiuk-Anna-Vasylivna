class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return f"Привіт, мене звуть {self.name}"

class Student(Person):
    def __init__(self, name, is_student=True):
        super().__init__(name)
        self.is_student = is_student

    def is_student_status(self):
        return self.is_student

student = Student("Анна")

print(student.greet())
print(f"Статус студента: {student.is_student_status()}")