"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число
- Оценки - список из целых чисел, может быть пустым

Опишите класс Student и метод avg_rate так, чтобы считалась средняя оценка, а при пустом списке оценок возвращался 0

"""


class Student:
    """Класс для представления студента."""

    def __init__(self, name: str, course: str, rating: list[int]):
        """Конструктор, инициализирующий экземпляр класса Student. Принимает name, course, rating."""

        self.name = name
        self.course = course
        self.rating = rating

    def avg_rate(self):
        """Метод, возвращающий среднюю оценку студента за курс."""

        try:
            print(sum(self.rating) / len(self.rating))
        except ZeroDivisionError:
            print(0.0)


# код для проверки
student = Student('Ivan', 'Python', [5, 4, 5, 5])
student.avg_rate() # 4.75

student = Student('Ivan', 'Python', [])
student.avg_rate() # 0.0
