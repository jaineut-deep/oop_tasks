class Librarians:
    """Методы-сеттеры и методы-геттеры -> это спецметоды, использующиеся для управления доступом к
    атрибутам класса. Геттеры позволяют получить доступ к атрибутам, а сеттеры -> изменить их."""

    def __init__(self, first, last):
        self.first: str = first
        self.last: str = last
        self._email: str = f"{self.first}-{self.last}@mail.ru"

    def get_email(self) -> str:
        """Получаем значение защищенного(protected) атрибута _email"""

        return self._email

    def set_email(self, email: str) -> None:
        """Задаем правило изменения защищенного атрибута _email"""

        self._email = email


class Lawyer:
    """Декоратор @property позволяет определить метод, к которому мы можем обращаться,
    как к атрибуту свойства."""

    def __init__(self, first, number, spec):
        self.first: str = first
        self.number: str = number
        self.spec: str = spec

    @property
    def email(self) -> str:
        """Возвращаем полный email из атрибутов класса. Можно обращаться без ().
        Если используется без setter - то только для чтения"""

        return f"{self.first}-{self.number}-{self.spec}@gmail.com"

    @property
    def fullname(self):
        """Возвращаем полное обозначение специалиста. Опять - без ().
        Декоратор @property указывается перед геттером, а не setter или deleter."""

        return f"{self.first}: {self.number}"

    @fullname.setter
    def fullname(self, forename):
        """Свойства выглядят как обычные атрибуты класса, но: при чтении - геттер,
        при записи - setter, при удалении - deleter. Метод срабатывает при операции
        присваивании"""

        first, number = forename.split("/")
        self.first = first
        self.number = number

    @fullname.deleter
    def fullname(self) -> None:
        """Через @property указываем, что происходит когда удаляем атрибут"""

        print("Delete Fullname!")
        self.first = None
        self.number = None
        self.spec = None


linguist = Librarians("Murdok", "Aelfey")
print(linguist.first)
print(linguist.last)
print(linguist.get_email())
print()
linguist.set_email(email=f"{linguist.first}-Lansk@mail.ru")
print(linguist.first)
print(linguist.last)
print(linguist.get_email())
print("INTERCLASSION")
my_lawyer = Lawyer("Konstantine", "897634", "admin")
print(my_lawyer.first)
print(my_lawyer.email)
print(my_lawyer.fullname)
print()
my_lawyer.first = "Fred"
print(my_lawyer.first)
print(my_lawyer.email)
print(my_lawyer.fullname)
print()
my_lawyer.fullname = "Arnold/3456719"
print(my_lawyer.fullname)
print()
del my_lawyer.fullname
print(my_lawyer.fullname)
print(my_lawyer.spec)
print(my_lawyer.email)
