"""
Для класса Employee и Client, опишите магический метод сложения таким образом, чтобы результатом сложения
было число, а прибавлять можно было только числа или другие объекты дочерних классов Employee

"""


class Employee:
    """Класс для представления сотрудника."""

    def __init__(self, pay):
        """Конструктор, инициализирующий экземпляр класса Employee."""

        self.pay = pay

    def __add__(self, other):
        """Метод, складывающий объекты наследуемые от класса Employee."""

        if isinstance(other, int | float):
            return self.pay + other
        else:
            raise TypeError


class Client:
    """Класс для представления клиента."""

    def __init__(self, pay):
        """Конструктор, инициализирующий экземпляр класса Client."""

        self.pay = pay

    def __add__(self, other):
        """Метод, складывающий объекты наследуемые от класса Client."""

        if isinstance(other, int | float):
            return other
        else:
            raise TypeError


class Developer(Employee):
    """Класс для представления разработчика от класса Employee."""

    def __init__(self, pay):
        """Конструктор, инициализирующий экземпляр класса Developer от класса Employee."""

        super().__init__(pay)

    def __add__(self, other):
        """Метод, складывающий объекты наследуемые от класса Employee."""

        return super().__add__(other)


class Manager(Employee):
    """Класс для представления управляющего от класса Employee."""

    def __init__(self, pay):
        """Конструктор, инициализирующий экземпляр класса Manager от класса Employee."""

        super().__init__(pay)

    def __add__(self, other):
        """Метод, складывающий объекты наследуемые от класса Employee."""

        return super().__add__(other)


# код для проверки
users = [Employee(50000), Client(100000), Developer(50000), Manager(50000)]

total_salary = 0
for user in users:
    total_salary = user + total_salary

print(total_salary)
# Вывод: 150000
