"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    """Класс для представления геометрической фигуры."""

    def __init__(self, name: str):
        """Конструктор, инициализирующий экземпляр класса Shape."""

        self.name = name

    def area(self) -> int | None:
        """Метод, который вычисляет площадь геометрической фигуры класса Shape."""

        if self.name:
            return 0
        else:
            return None


class Rectangle(Shape):
    """Класс, наследующийся от класса Shape, для представления прямоугольника."""

    def __init__(self, name: str, width: int | float, height: int | float):
        """Конструктор, инициализирующий экземпляр класса Rectangle. Принимает имя прямоугольника, ширину и высоту."""

        super().__init__(name)
        self.width = width
        self.height = height

    def area(self) -> int | None:
        """Метод, вычисляющий площадь прямоугольника класса Rectangle."""

        if self.height and self.width:
            return self.height * self.width
        else:
            return None


class Triangle(Shape):
    """Класс, наследующийся от класса Shape, для представления треугольника."""

    def __init__(self, name: str, base: int | float, height: int | float):
        """Конструктор, инициализирующий экземпляр класса Rectangle. Принимает имя треугольника, основание и высоту."""

        super().__init__(name)
        self.base = base
        self.height = height

    def area(self) -> int | None:
        """Метод, вычисляющий площадь треугольника класса Triangle."""

        if self.base and self.height:
            square = (self.base * self.height) / 2
            return round(square)
        else:
            return None


# код для проверки 
shape = Shape("Shape")
print(shape.area())  # 0

rect = Rectangle("Rectangle", 5, 10)
print(rect.area())  # 50

tri = Triangle("Triangle", 6, 4)
print(tri.area())  # 12
