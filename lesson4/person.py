"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Student, наследующийся от класса Person, представляющий студента, имеющий следующие методы:

- __init__(self, name, age, major): конструктор, принимающий имя студента, его возраст и основной предмет
- get_major(self): метод, который возвращает основной предмет студента.
"""


class Person:
    """Класс для представления человека."""

    def __init__(self, name: str, age: int):
        """Конструктор, инициализирующий экземпляр класса Person. Принимает аргументы имени и возраста для человека."""

        self.name = name
        self.age = age

    def get_name(self):
        """Метод, возвращающий имя человека."""

        return self.name

    def get_age(self):
        """Метод, возвращающий возраст человека."""

        return self.age


class Student(Person):
    """Класс для представления студента."""

    def __init__(self, name, age, major):
        """Конструктор, инициализирующий экземпляр класса Student, дочернего Person."""

        super().__init__(name, age)
        self.major = major

    def get_major(self):
        """Метод, возвращающий основной предмет студента."""

        return self.major


# код для проверки 
person = Person("Иван", 25)
print(person.get_name())  # Иван
print(person.get_age())  # 25

student = Student("Мария", 20, "математика")
print(student.get_name())  # Мария
print(student.get_age())  # 20
print(student.get_major())  # математика
