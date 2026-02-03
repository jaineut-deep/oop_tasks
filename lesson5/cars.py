"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходит получение, присваивание и удаление значения.
"""


class Car:
    """Класс для представления автомобиля."""

    def __init__(self, brand: str, model: str, release_year: int):
        """Конструктор, инициализирующий экземпляр класса Car. Принимает аргументы: бренд, модель и год выпуска автомобиля."""

        self.brand = brand
        self.model = model
        self.release_year = release_year

    def get_set_del(self):
        """Метод, изменяющий параметры экземпляра класса Car."""

        self.brand += "V2"
        self.model = "NewCar"
        self.release_year = 2020


class CarSlots:
    """Класс для представления автомобиля с локализованными параметрами."""

    __slots__ = ("brand", "model", "release_year")

    def __init__(self, brand: str, model: str, release_year: int):
        """Конструктор, инициализирующий экземпляр класса CarSlots. Принимает аргументы: бренд, модель и год выпуска автомобиля."""

        self.brand = brand
        self.model = model
        self.release_year = release_year

    def get_set_del(self):
        """Метод, изменяющий параметры экземпляра класса CarSlots."""

        self.brand += "V2"
        self.model = "NewCar"
        self.release_year = 2020


car = Car('Toyota', 'Corolla', 2022)
car_slots = CarSlots('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del, number=1)
t2 = timeit.timeit(car_slots.get_set_del, number=1)
print(f"{((t1 - t2) / t1) * 100:.2f}%")
