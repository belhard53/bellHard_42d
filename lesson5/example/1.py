# c = 1
# c2 =c
# c2 = 2 # первоисточник не поменяется
# print(c, c2)

# a = [1,2,9,3,4, []]
# b = a
# b.append(1) # первоисточник поменяется
# print(b)

# from copy import deepcopy
# a = [1,2,9,3,4, []]
# b = list(a)  # повехностная копия
# b = a.copy() # аналогично предыдущей строке 
# с = deepcopy(a) # глубока я копия
# a[-1].append(123)
# b.append(5)

# print(a)
# print(b)
# print(с)


# d = {}
# d = dict()
# d = {1:123, 'name_usere':'Dmitri', True:"123", 
#      2:"python", "2":"hello", "list_item":[1, 2, 3, 4]}
# print(d['2'])
# print(d[2])

# users = ['vasia', 'vasiapupkin', '3752323232']
# user1 = {'name':'vasia', 'surname':'vasiapupkin', 'phone':'3752323232'}
# user2 = {'name':'DIma', 'surname':'DimaKrivenyz', 'phone':'3752323232'}
# user2['name'] = 'Dima'
# user2['age'] = 32

# users1 = {
#     'user1':user1,
#     'user2':user1,
# }
# users2 = {
#     1:user1,
#     2:user1,
# }
# users3 = [user1, user2]

# print(users3)
# print(users1)
# print(users1['user1'])
# print(users1['user1']['name'])
# print(users2[1])
# print(users3[1])

# users4 = [
#     {
#         'name':'vasia', 
#         'surname':'vasiapupkin', 
#         'phone':'3752323232'
#     },
#     {'name':'DIma', 
#      'surname':'DimaKrivenyz', 
#      'phone':'3752323232'}
# ]
# user5 = {
#     'name':'vasia', 
#     'surname':'vasiapupkin', 
#     'phone':'3752323232',
#     'projects':{"name":"qwqw", "lang":['py', 'html', 'css']}
# }

# print(user5.get('name1', "Нет такого ключа"))
# user5['age'] = 31
# #user5.clear()
# #user5.fromkeys()
# print(list(user5.keys()))
# print(user5.values())
# print(list(user5.items())[1])
# print(list(user5.items())[1][1])

# del user5['age']

# print(user5)

# user6 = {"qww":'sasas', **user5, 1:2, **user2}
# user6 = user5 | user2
# print(user6)

# data = {"sep": "-", "end": " FINISH!"}
# print(1, 2, 3, 4, 5, **data) # распаковка слловаря как параметров 

# кортежи
# cor = (23, 43)
# x, y = cor

# a = (1,2,3,4,5,6,7)
# b, *c, e = a
# print(a)
# print(b)
# print(c)
# print(e)

# a1 = (*a, 8, 9)

# a = (1,)
# a = tuple([1, 2, 3, 4])
# a[1] = 4 # ошибка
# a = 1, 2, 3


# Множества
# l = [1, 2, 3, 2, 3, 1, 6, 3, 2]
# a = set()
# a = set(l)
# print(a)
# a = {1,2,3,4,1,2,3,5,2}
# print(a)
# a = set('hello')
# print(a)

# a = {8, 3, 1, 5 }
# b = {6, 7, 8, 3}
# # b = {8, 1, 3}

# print(a.issuperset(b))
# print( a >= b )

# #объединение и пересечение

# print(a | b) # обьеденить
# print(a.union(b)) # обьеденить

# print(a.intersection(b)) # только общие

# print(a.difference(b)) # есть только в первом
# print(a & b )

# print(a.symmetric_difference(b)) # есть в обоих но не общие
# print(a ^ b)




# from collections import *

# words = ["Hello", "World", "Hello", "Python"]
# c = Counter(words)
# b = Counter(["Hello", "World", "Python", "World", "Pycharm"])
# print(c)
# print(b)
# # c.subtract(b)
# print(c - b)


# data = defaultdict(int)
# data["a"] += 5
# print(data)
# User = namedtuple("User", ["name", "age", "city"])
# vasya = User(name="Vasya", age=34, city="Minsk")
# petya = User(name="Petya", age=32, city="Gomel")
# print(vasya.name)
# print(petya.name)
# print(vasya._asdict())


# numbers = deque([1, 2, 3, 4, 5])
# numbers.rotate(-2)
# print(numbers)

# a = {1: 1, 2: 2, 3: 3}
# b = {3: 4, 4: 5, 5: 6}
# chain = ChainMap(a, b)
# # print(chain.parents[3])
# chain["text"] = "Hello"
# print(chain)

# a = [1, 2]
# b = [1, 2, 3]
# print(a < b)


