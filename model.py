# • model.py: Содержит классы Student, Course и School. Student и
# Course управляют данными о студентах и курсах, а School управляет
# коллекцией студентов и курсов.

import uuid

class Student:
    def __init__(self, name, year):
        self.name = name
        self.id = str(uuid.uuid4())[:6]
        self.year = year
        self.courses = []

    def __str__(self):
        courses = ', '.join(c.name for c in self.courses) or 'нет'
        return f"{self.name} | ID: {self.id} | Год: {self.year} | Курсы: {courses}"

class Course:
    def __init__(self, name):
        self.name = name
        self.id = str(uuid.uuid4())[:6]
        self.students = []

    def __str__(self):
        return f"{self.name} | ID: {self.id} | Студентов: {len(self.students)}"

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)
        return True

    def add_course(self, course):
        self.courses.append(course)
        return True

    def enroll(self, student_id, course_id):
        student = self.find_student(student_id)
        course = self.find_course(course_id)
        if student and course:
            student.courses.append(course)
            course.students.append(student)
            return True
        return False

    def find_student(self, student_id):
        for s in self.students:
            if s.id == student_id:
                return s
        return None

    def find_course(self, course_id):
        for c in self.courses:
            if c.id == course_id:
                return c
        return None
