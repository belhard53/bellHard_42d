from typing import Any

# абстракция
# наследование
# полиморфизм
# инкапсуляция


# наследование
# class A():
#     a = 1
#     def __init__(self, b) -> None:
#         self.b = b

# class B(A):
#     pass
    
# a = A(2)
# b = B(3)

# print(a.b)
# print(b.b, b.a)


# class MyList(list):
#     def slice(self, n):
#         for i in range(n):
#             self.insert(0, self.pop())

      ## переписали метод appepnd - теперь он вставляет не в конец а в начало       
#     def append(self, __object: Any) -> None:
#         self.insert(0, __object)
        

# a = MyList()
# a += [1,2,3,4,5,6]
# a.append(7)
# # a.slice(3)
# print(a)


# Множественное наследование

# class A:
#     def __init__(self) -> None:
#         a = 1
#         print("A")

# #mixin
# class A2:
#     def print_info2():
#         print(111)

# class B:
#     def __init__(self) -> None:
#         a = 2
#         print("B")

# class C(A, B, A2):    
#     def __init__(self) -> None:
#         A.__init__(self)
#         B.__init__(self)
#         print('C')
#         c = 3
        
  
# c = C()
# c.print_info2()



# инкапсуляция

# class User:   
#     __age: int = 0    
#     __flag = False
    
#     def __check_age(self, age):
#         return age >= 14
    
#     # @staticmethod
#     # def check_age(age):
#     #     return age >= 14
    
#     def __init__(self, name, age):
#         self.name = name
#         if not self.__check_age(age):
#             raise ...
#         self.__age = age
    
    
#     @property #getter  
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, val):
#         if self.__check_age(val):
#             self.__age = val
#         else:
#             raise ValueError ("Возраст меньше 14")
    
#     def change_type(self):
#         self.__flag = not self.__flag
    
#     def add_age(self):
#         self.age += 1
    



# print(user.__flag) # ошибка
# user.change_type()

# user = User('Max', 22)
# print(user.age)
# user.age = 6
# print(user.age)

# # user.__age = 6
# # print(user.age)

# # print(user._age)
# # print(user.__age)


# # Утиная типизация

# class A:
#     def foo1(self):
#         print(1)
#     def __len__(self):
#         return 1
    
# class B:
#     def foo1(self):
#         print(2)
#     def __len__(self):
#         return 2

# def f1(obj):
#     obj.foo1()
        
# a = A()
# b = B()

# f1(a)
# f1(b)

# l = [A(), B(), A(), "sas"]
# print(list(map(len, l)))
# for obj in l:
#     try:
#         obj.foo1()
#     except:
#         print('err')
        
        
# # абстрактные классы 
# # только для наследования
# from abc import ABC, abstractmethod

# class Basic(ABC):
#     __slots__ = ['a','b']
    
#     @abstractmethod
#     def foo1(self):
#         print(1)


# class Child(Basic):
    
#     def foo1(self):
#         super().foo1()
#         print(2)
        

# # a = Basic()
# b = Child()
# # a.foo1()
# b.foo1()        


        
        

# # декораторы класса
# def class_decorator(cls):
#     attrs = dict(a=1, b=2, c=3)
#     for attr, val in attrs.items():
#         setattr(cls, attr, val) 
#     return cls

# @class_decorator
# class A:
#     def a():
#         print(1)
        
        
# a = A()    
# print(a.a, a.b)	



# датакласы - упрощенные классы для создания структуры

from dataclasses import dataclass

# @dataclass(frozen=True)
@dataclass()
class User:
    # получаем упрощенную запись класса
    # с реализованными методами __init__, __repr__, __str__ и __eq__
         
    # аннотации типов обязательны
    name:str
    age:int
    a: Any
    
user = User('Alex', 33, 1)
user.age = 20

users = [
    user,
    User("Max", 20, '1'),
    User("Djo", 20, True)
]

for user in users:
    print(user)
    # user.send_email()
    