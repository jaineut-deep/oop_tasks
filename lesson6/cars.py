"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Важно в конструкторе обрабатывать исключения, если год больше текущего
"""
from datetime import date


class Car:
    """Класс для представления машины."""

    def __init__(self, brand, model, release_year):
        """Конструктор, инициализирующий экземпляр класса. Принимает бренд, модель и год выпуска."""

        self.brand = brand
        self.model = model
        if release_year > date.today().year:
            raise Exception("Эта машина еще не была выпущена")
        self.release_year = release_year


# код для проверки
car = Car('Toyota', 'Corolla', 2022)

car_two = Car('Toyota', 'Corolla', 3000)
# raises Exception('Эта машина еще не была выпущена')
