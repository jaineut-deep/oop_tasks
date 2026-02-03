"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "Flying".

Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".

Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:

- hunt(self): метод, который выводит сообщение "Hunting".
"""


class Bird:
    """Класс для представления птицы."""

    def fly(self):
        """Метод, который выводит сообщение "Flying"."""

        print("Flying")


class Penguin(Bird):
    """Класс для представления пингвина."""

    def fly(self):
        """Метод, который выводит сообщение "I am a penguin and cannot fly"."""

        print("I am a penguin and cannot fly")


class Eagle(Bird):
    """Класс для представления орла."""

    def hunt(self):
        """Метод, метод, который выводит сообщение "Hunting"."""

        if self:
            print("Hunting")


# код для проверки 
bird = Bird()
bird.fly()  # Flying

penguin = Penguin()
penguin.fly()  # I am a penguin and cannot fly

eagle = Eagle()
eagle.fly()  # Flying
eagle.hunt()  # Hunting
