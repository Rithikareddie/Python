
class Person:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
    

class Student(Person):
    def __init__(self, name, age, id, dept):
        self.dept = dept
        super().__init__(name, age, id)


class Employee(Person):
    def __init__(self, name, age, id, dept, salary, role, subject):
        self.salary = salary
        self.role = role
        self.subject = subject
        super().__init__(name, age, id, dept)


class University(Student, Employee):
    def __init__(self, university_name, course_name=[b.tech,m.tech], student_data={}, employee_data={}):
        self.university_name = university_name
            