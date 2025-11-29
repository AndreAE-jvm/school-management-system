# • controller.py: Содержит класс SchoolController, который управляет
# взаимодействием между моделью и представлением. Метод main() создает
# экземпляры модели, представления и контроллера, а затем запускает меню для
# взаимодействия с пользователем.

from model import Student, Course

class SchoolController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
        while True:
            self.view.show_menu()
            choice = self.view.get_choice()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_course()
            elif choice == "3":
                self.enroll()
            elif choice == "4":
                self.show_students()
            elif choice == "5":
                self.show_courses()
            elif choice == "6":
                break
            else:
                self.view.show_msg("Неверный выбор")

    def add_student(self):
        name, year = self.view.get_student()
        student = Student(name, year)
        self.model.add_student(student)
        self.view.show_message(f"Студент {name} добавлен. ID: {student.id}")

    def add_course(self):
        name = self.view.get_course()
        course = Course(name)
        self.model.add_course(course)
        self.view.show_message(f"Курс {name} добавлен. ID: {course.id}")

    def enroll(self):
        student_id, course_id = self.view.get_enroll()
        if self.model.enroll(student_id, course_id):
            self.view.show_message("Студент записан на курс")
        else:
            self.view.show_message("Ошибка")

    def show_students(self):
        self.view.show_list(self.model.students, "Студенты")

    def show_courses(self):
        self.view.show_list(self.model.courses, "Курсы")