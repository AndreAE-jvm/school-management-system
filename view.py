# • view.py: Содержит класс SchoolView, который отвечает за
# взаимодействие с пользователем: отображение студентов и курсов, вывод
# сообщений и получение данных от пользователя.

class SchoolView:
    def show_menu(self):
        print(f"\n1. Добавить студента\n"
              f"2. Добавить курс\n"
              f"3. Записать на курс\n"
              f"4. Список студентов\n"
              f"5. Список курсов\n"
              f"6. Выход\n")

    def get_choice(self):
        return input("Выберите: ")

    def get_student(self):
        name = input("Имя: ")
        year = input("Год: ")
        return name, year

    def get_course(self):
        return input("Название курса: ")

    def get_enroll(self):
        student_id = input("ID студента: ")
        course_id = input("ID курса: ")
        return student_id, course_id

    def show_list(self, items, title):
        if not items:
            print(f"{title} нет")
        else:
            print(f"\n{title}:")
            for item in items:
                print(f"• {item}")

    def show_message(self, message):
        print(message)
