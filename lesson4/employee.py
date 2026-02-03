"""
Напишите класс Employee, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, salary): конструктор, принимающий имя сотрудника и его зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, salary, bonus): конструктор, принимающий имя менеджера, его зарплату и бонус;
- get_salary(self): метод, который возвращает зарплату менеджера плюс его бонус.
"""


class Employee:
    """Класс для представления сотрудника."""

    def __init__(self, name, salary):
        """Конструктор, инициализирующий экземпляр класса: принимает имя сотрудника и его зарплату."""

        self.name = name
        self.salary = salary

    def get_salary(self):
        """Метод, который возвращает зарплату сотрудника."""

        return self.salary


class Manager(Employee):
    """Класс, наследующийся от класса Employee, представляющий менеджера."""

    def __init__(self, name, salary, bonus):
        """Конструктор, инициализирующий экземпляр класса Manager, дочернего классу Employee: принимает имя,
        зарплату и бонус менеджера.
        """

        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        """Метод, который возвращает зарплату менеджера плюс его бонус."""

        return super().get_salary() + self.bonus


# код для проверки 
employee = Employee("John", 5000)
print(employee.get_salary())  # 5000

manager = Manager("Jane", 10000, 5000)
print(manager.get_salary())  # 15000
