"""
Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"

Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
Выполняеся функция <имя> с аргусентами <аргументы> 
После выполнения функции напечатать строку "<имя функции> - завершена"
"""


def decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Выполняем функцию {func.__name__} c аргс {args} b c кваргс {kwargs}")
        func(*args, **kwargs)
        print(f"Выподнено {func.__name__}")
    return wrapper

@decorator
def hello12(name, surname, v1=True, v2=2):
    print(f"Привет {surname} {name} {'!' if v1 else ''}")

name = "Иван"
surname = "Иванов"

hello12(name, surname)