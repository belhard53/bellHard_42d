"""
Написать декоратор который позволит не останавливать программу 
в случае если любая декорируемая функция выбрасывает ошибку, 
а выводить имя функции в которой произошла ошибка и информацию об ошибке в консоль. 
Имя функции можно узнать использовав свойство __name__ ( print(func.__name__) )
"""


def err_log(func):
    def wrapper(*args, **kwargs):        
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"При выполнении функции {func.__name__} произошла ошибка\n"\
                  f"{e}")
            
        
    return wrapper

@err_log
def f1(a):
    print(100/a)

for i in [1,2,0,3,4]:
    f1(i)

    