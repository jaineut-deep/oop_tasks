"""
Напишите класс User, имеющий следующие свойства и методы:

- __init__(self, name, password): конструктор, принимающий имя пользователя и пароль
- name: свойство, которое возвращает имя пользователя
- password: свойство, которое позволяет установить или изменить пароль пользователя
- is_admin: свойство, которое возвращает, является ли пользователь администратором или нет
- _is_admin: свойство-помощник, которое определяет, является ли пользователь администратором или нет
- login(self, password): метод, который проверяет, соответствует ли введенный пароль паролю пользователя
- logout(self): метод, который выходит из аккаунта пользователя (устанавливает значение свойства _is_logged_in в False при условии, что пользователь залогинен)

Для свойств name и password используйте декораторы @property и @password.setter.
"""


class User:
    """Класс для представления пользователя"""

    admin = ""
    session = set()

    def __init__(self, name, password):
        self._name = name
        self._password = password

    @property
    def name(self):
        return f"{self._name}"

    @property
    def password(self):
        return f"{self._password}"

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def is_admin(self):
        if self._name == self.admin:
            return True
        return False

    @property
    def _is_admin(self):
        return

    @_is_admin.setter
    def _is_admin(self, status):
        if str(status) == "True":
            self.admin = self.name
        elif str(status) == "False" and self.admin == self._name:
            self.admin = ""

    def _is_logged_in(self):
        if self.name in self.session:
            return True
        return False

    def login(self, password):
        if password == self._password and self._name not in self.session:
            self.session.add(self._name)
            print(True)
        elif password == self._password and self._name in self.session:
            print(True)
        return False

    def logout(self):
        self.session.discard(self._name)


# код для проверки 
user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
