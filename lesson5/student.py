"""
Напишите класс Student, представляющий студента, имеющий следующие атрибуты:

- __slots__ = ('name', 'age', 'grades'): список атрибутов, доступных объекту.

Напишите класс Course, представляющий курс, имеющий следующие атрибуты:

- __slots__ = ('name', 'students'): список атрибутов, доступных объекту.
"""


class Student:
    """Класс для представления студента."""

    __slots__ = ("name", "age", "grades")

    def __init__(self, name: str = None, age: int = None, grades: int = None):
        """Конструктор, инициализирующий экземпляр класса Student."""

        self.name = name
        self.age = age
        self.grades = grades


class Course:
    """Класс для представления курса."""

    __slots__ = ("name", "students")

    def __init__(self, name: str = None, students: list = None):
        """Конструктор, инициализирующий экземпляр класса Course."""

        self.name = name
        self.students = students


# код для проверки 
student1 = Student()
student1.name = "John"
student1.age = 20
student1.grades = [90, 80, 85]

student2 = Student()
student2.name = "Jane"
student2.age = 21
student2.grades = [95, 85, 90]

course = Course()
course.name = "Math"
course.students = [student1, student2]


if __name__ == "__main__":
    for idx in course.students:
        print(idx.grades)
