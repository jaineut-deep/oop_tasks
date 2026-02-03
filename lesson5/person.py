"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Employee2, наследующийся от класса Person, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, age, salary): конструктор, принимающий имя сотрудника, его возраст и зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager2, наследующийся от класса Employee2, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, age, salary, bonus): конструктор, принимающий имя менеджера, его возраст, зарплату и бонус;
- get_bonus(self): метод, который возвращает бонус менеджера.
"""


class Person:
    """Класс для представления человека."""

    def __init__(self, name, age):
        """Конструктор, инициализирующий экземпляр класса Person. Принимает имя и возраст человека."""

        self.name = name
        self.age = age

    def get_name(self):
        """Метод, возвращающий имя человека."""

        return self.name

    def get_age(self):
        """Метод, возвращающий возраст человека."""

        return self.age


class Employee2(Person):
    """Класс, дочерний классу Person, для представления сотрудника."""

    def __init__(self, name, age, salary):
        """Конструктор, инициализирующий экземпляр класса Employee2. Принимает имя, возраст и зарплату сотрудника."""

        super().__init__(name, age)
        self.salary = salary

    def get_salary(self):
        """Метод, возвращающий зарплату сотрудника."""

        return self.salary


class Manager2(Employee2):
    """Класс, дочерний классу Employee2, для представления менеджера."""

    def __init__(self, name, age, salary, bonus):
        """Конструктор, инициализирующий экземпляр класса Manager2. Принимает имя, возраст, зарплату и бонус менеджера."""

        super().__init__(name, age, salary)
        self.bonus = bonus

    def get_bonus(self):
        """Метод, возвращающий бонус менеджера."""

        return self.bonus


# код для проверки 
person = Person("John", 30)
print(person.get_name())  # John
print(person.get_age())  # 30

employee = Employee2("Jane", 25, 5000)
print(employee.get_name())  # Jane
print(employee.get_age())  # 25
print(employee.get_salary())  # 5000

manager = Manager2("Bob", 40, 10000, 5000)
print(manager.get_name())  # Bob
print(manager.get_age())  # 40
print(manager.get_salary())  # 10000
print(manager.get_bonus())  # 5000
