class Student:
    def __init__(self, student_id, name,
                 course, semester, phone, email):

        self.student_id = student_id
        self.name = name
        self.course = course
        self.semester = semester
        self.phone = phone
        self.email = email

    def display_student(self):
        return {
            "Student ID": self.student_id,
            "Name": self.name,
            "Course": self.course,
            "Semester": self.semester,
            "Phone": self.phone,
            "Email": self.email
        }
