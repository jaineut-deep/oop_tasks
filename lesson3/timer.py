"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
import time


class Timer:
    """Класс для представления таймера."""

    def __enter__(self):
        """Магический метод, запускающий таймер."""

        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Магический метод, останавливающий таймер и выводящий время выполнения блока кода."""

        self.end = time.time()
        self.elapsed_time = self.end - self.start


with Timer() as timer:
    total = 0
    for i in range(1000000):
        total += i
    
    # код для проверки 
print("Execution time:", timer.elapsed_time)
