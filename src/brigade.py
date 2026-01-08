class Worker:
    """Класс для представления сотрудника."""

    index = 1.1
    workers_count = 0

    name: str
    surname: str
    age: int
    pay: float
    place: str

    def __init__(self, name, surname, age, pay):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""

        self.name = name
        self.surname = surname
        self.age = age
        self.pay = pay
        self.place = f"{name}_{surname}.block2A1floor"

        Worker.workers_count += 1


    def pay_upgrade(self):
        """Метод, возвращающий проиндексированное значение заработной платы сотрудника."""

        self.pay = round((self.pay * self.index), 2)


fellow_1 = Worker("Ingvar", "Broneldsen", 23, 65000)
fellow_2 = Worker("Folgunthur", "Heilmden", 28, 49000)

print(f"Name: {fellow_1.name}")
print(f"Surname: {fellow_1.surname}")
print(f"Age: {fellow_1.age}")
print(f"Place: {fellow_1.place}")
print()
print(f"Name: {fellow_2.name}")
print(f"Surname: {fellow_2.surname}")
print(f"Age: {fellow_2.age}")
print(f"Place: {fellow_2.place}")
print()
fellow_1.pay_upgrade()
fellow_2.pay_upgrade()
print(f"{fellow_1.name} pay: {fellow_1.pay}")
print(f"{fellow_2.name} pay: {fellow_2.pay}")
print()
print(f"Count_of_workers: {Worker.workers_count}")
print(fellow_1.index)
