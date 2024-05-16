# def print3(*args):
#     print(args)

# print3('Hello', 'Python', 1, 5)


# def print_user(**kwargs):
#     print(kwargs)
    
# print_user(name='Dima', age=20, login='vasia123')
    

# def f1(a, b, *args, **kwargs):
#     print(a, b, args, kwargs, sep='\n')
    
# f1(1, 3, 4, 5, 6, 7, q=1, w='Hello')


# def baz2(e, *, a, b, c, d):
# #     print(a)
# #     print(b)
# #     print(c)
# #     print(d)
# #     print(e)
# #
# #
# # # baz2(0, a=1, b=2, c=3, d=4)



#-------------- type hints - тайпхинтинг
# def f2(a:int | float, b: str, c: list[int|float]) -> bool:
#     print(a)
    
# f2("1", "H", [1,2])


# def foo(a: list, *args: str | int, **kwargs: int) -> tuple[bool, bool]:
#     print(a)
#     print(args)
#     print(kwargs)
#     return True, False

# numbers: list[int] = [1, 2, 3, 4]
#
# data: dict[str, dict[str, str]] = {
#     "name": {"min": "Alex"}
# }
#
## ----------- внутренние свойства функций 
# def bar(objs: list):
#     for obj in objs:  # type: int
#         print(obj)
#
#
# print(bar.__annotations__)
# print(bar.__name__)
# print(bar.__code__)
# print(bar.__builtins__)
# print(bar.__dict__)


# ---------- передача функции в качестве параметра
# def ff1(f):
#     f("123")
    
# ff1(print)


# ------------ замыкание 
# def f1(a):
#     def f2(b):
#         return a*b
#     return f2

# a_1 = f1(1)
# a_3 = f1(2)
# print(a_2(5))
# print(a_3(5))

# def print1(a):
#     def wrapper(b):
#         print(f"{a}{' - ' if a else ''}{b}")
#     return wrapper
# pr_err = print1("Error")
# pr_info = print1("Внимание")
# pr = print1("")
# pr_err("Пароль неверный")
# pr_info("В пароле должно быть более 7 символов")
# pr("Ok")
        


# декораторы
# from time import time

# def check_time(f):
#     def wrapper(*args, **kwargs):
#         start = time()     
#         print('start', f.__name__)
#         res = f(*args, **kwargs)
#         end = time()
#         print('Время - ', end - start) 
#         print('end')
#         return res
#     return wrapper

# # @loging - можно несколько декораторов
# @check_time    
# def f3(a, b):
#     return a**b

# print(f3(10, 5))

# ------------------- генераторы
# l = (i*2 for i in range(2, 100, 3))
# print(l)
# print(type(l))

# print(next(l))
# print(next(l))
# print(next(l))


# def  f4():
#     yield 1
#     yield 2
#     yield 10
#     yield 15
    
# g = f4()    
# print(g[1]) - ошибка - по индексу получить нельзя - только следующий
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))


# def f5(n):
#     for i in range(n):
#         yield i**2 + 25+ 1 * i
        
# for i in f5(5):
#     print(i)

# def f6():
#     i = 3 
#     while 1:
#         i *= 2
#         yield i

# g = f6()        
# for i in range(10):
#     print(next(g))
    
