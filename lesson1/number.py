"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    """Класс, представляющий число, его сумму и его разность с другим числом"""

    def __init__(self, value: int):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра"""

        self.value = value

    def get(self):
        """Мотод, возвращающий значение указанного экземпляра(целого числа)"""

        return self.value

    def add(self, num):
        """Метод, возвращающий сумму экземпляра(целого числа) и целого числа"""

        self.value = self.value + num
        return self.value

    def substract(self, num):
        """Метод, возвращающий разность экземпляра(целого числа) и целого числа"""

        self.value = self.value - num
        return self.value


# код для проверки 
n = Number(7)
print(n.get())  # 7
n.add(3)
print(n.get())  # 10
n.substract(5)
print(n.get())  # 5
