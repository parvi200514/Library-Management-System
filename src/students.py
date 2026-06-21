class Student:
    def __init__(self, student_name, course, semester, phone, email):
        self.student_name = student_name
        self.course = course
        self.semester = semester
        self.phone = phone
        self.email = email

    def add_student(self):
        return f"Student '{self.student_name}' added successfully."
