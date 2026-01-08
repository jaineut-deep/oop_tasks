import datetime
from typing import Self
from datetime import date


class HardWorker:
    """Класс для представления рабочего"""

    rise_index: float = 1.1
    state_count = 0

    def __init__(self, first: str, last: str, pay: str):
        self.first = first
        self.last = last
        self.email: str = first + "-" + last + "@mail.ru"
        self.pay = float(pay)

        HardWorker.state_count += 1

    def overall_name(self) -> str:
        return f"{self.first} {self.last}"

    def apply_raise(self) -> None:
        self.pay = round((self.pay * self.rise_index), 2)

    @classmethod
    def full_character(cls, lean_line: str) -> Self:
        first, last, pay = lean_line.split("-")
        return cls(first, last, pay)

    @classmethod
    def indexing_pay(cls, add_pay: float) -> None:
        cls.rise_index = add_pay

    @staticmethod
    def is_job(day: datetime.date) -> bool:
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True


worker_one = HardWorker("Jeremy", "Soule", "100000.20")
worker_two = HardWorker("Alfred", "Dew", "78000.68")
HardWorker.indexing_pay(1.25)
print(f"Pay indexes: by class HardWorker - {HardWorker.rise_index},\nby objects - worker_one/{worker_one.rise_index}, "
      f"worker_two/{worker_two.rise_index}\n")
print(f"Worker's pay: worker_one - {worker_one.pay}, worker_two - {worker_two.pay}")
print()
HardWorker.apply_raise(worker_one)
HardWorker.apply_raise(worker_two)
print(f"Risen up pay: for worker_one - {worker_one.pay}, for worker_two - {worker_two.pay}")
print()
freelancer_one_str = "Malcolm-Starfield-45000.34"
freelancer_two_str = "Bartholomeus-Faut-53000.62"
freelancer_one = HardWorker.full_character(freelancer_one_str)
freelancer_two = HardWorker.full_character(freelancer_two_str)
print(f"New season employee: {freelancer_one.first} - {freelancer_one.email}, and\n"
      f"{freelancer_two.first} - {freelancer_two.email}")
print(f"Their pay: {freelancer_one.first} - {freelancer_one.pay}, {freelancer_two.first} - {freelancer_two.pay}")
print()
HardWorker.apply_raise(freelancer_one)
HardWorker.apply_raise(freelancer_two)
print(freelancer_one.pay)
print(freelancer_two.pay)
print()
info_line = "QA/QI-u/34-34000.59"
print(info_line)
description_name = HardWorker.full_character(info_line)
print(description_name.first)
print(description_name.last)
print(description_name.rise_index)
print(description_name.pay)
print()
HardWorker.apply_raise(description_name)
print(description_name.pay)
print(HardWorker.is_job(date.today()))
print(date.today())
print()
print(dir(worker_one))
