"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:
    """Класс для представления животного."""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def speak():
        """Метод, который выводит звук, издаваемый животным."""

        print("?")

class Dog(Animal):
    """Класс для представления собаки."""

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def speak():
        """Метод, который выводит звук, издаваемый собакой."""

        print("Woof!")


class Cat(Animal):
    """Класс для представления кошки."""

    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def speak():
        """Метод, который выводит звук, издаваемый кошкой."""

        print("Meow!")


# код для проверки 
animal = Animal("Animal")
animal.speak()  # ?

dog = Dog("Dog")
dog.speak()  # Woof!

cat = Cat("Cat")
cat.speak()  # Meow!
