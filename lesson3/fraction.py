"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    """Класс для представления дроби."""

    numerator: int
    denominator: int

    def __init__(self, numerator: int, denominator: int):
        """Конструктор инициализирующий экземпляр класса. Задает значения атрибутам экземпляра."""

        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        """Магический метод, возвращающий строковое представление дроби."""

        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        """Магический метод, возвращающий строковое представление дроби для пользователя."""

        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        """Магический метод, складывающий дроби и возвращающий новую дробь."""

        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)


# код для проверки 
fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
