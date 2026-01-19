"""
Напишите класс Logger, имеющий следующие методы:

- __init__(self, filename): конструктор, принимающий имя файла, в который будет производиться запись логов;
- __call__(self, message): магический метод, который позволяет использовать объект класса Logger как функцию,
принимающую сообщение и записывающую его в файл.
"""
import os


class Logger:
    """Класс для представления логгера."""

    filename: str
    message: str
    mode: str

    def __init__(self, filename: str, mode="a"):
        """Конструктор, задающий для экземпляра класса файл для логов."""

        self.filename = filename
        self.mode = mode

    def __call__(self, message: str):
        """Магический метод, вызывающий экземпляр класса как функцию для записи сообщений в файл."""

        file_name = os.path.dirname(os.path.dirname(__file__)) + "/data/" + self.filename
        with open(file_name, self.mode) as file:
            file.write(message + "\n")


# код для проверки 
logger = Logger("log.txt")
logger("This is a test message.")
