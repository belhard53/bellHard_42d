"""
Написать функцию счетчик которая с помощью замыкания 
будет хранить в себе количество запускови каждый раз возвращать число на 1 больше.
Функция должна принимать число с которого начинается отсчет.

Пример:
с1 = counter(1)
с10 = counter(10)

print(c1()) -> 2
print(c1()) -> 3
print(c1()) -> 4 

print(c10()) -> 11 
print(c10()) -> 12 
print(c10()) -> 13 

"""

def counter(n):
    def c_add():
        nonlocal n
        n += 1
        return n
    return c_add

c1 = counter(0)
c2 = counter(10)

print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
