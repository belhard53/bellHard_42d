# списки

# a = []
# b = list('hello')
# c = [1, 2, 3, 9, 5, "hello", True, 12, 45, "", 11.3, None]
# e = [111, 222, 333]


# print(c)
# print(*c, sep="--==--", end="конец списка\n")
# print(len(c))
# print(c[1:3]) # распечатать с индекса 1 до 3 (3 не влючительно)
# print(c[:3]) # распечатать с индекса 0 до 3 (3 не влючительно)
# print(c[::2])
# c[2] = 9
# c = c + e
# print(c)
# print(e*3)
# e += [1, 2]
# print(e)

# a = [1, 2, 3]
# a = []
# a.append(4)
# print(a)

# users = []
# user1 = ['Dima', 23, 'login', True, 'password', ['1221', '43430984'], ['py', ['html1', 'html3']]]
# user2 = ['Vasia', 23, 'login', False, 'password', ['54545', '5454545'], ['py', ['html4', 'html5']]]

# from pprint import pprint
# users.append(user1)
# users.append(user2)
#pprint(users)

# print(users)
# print(len(users))
# print(users[1][4][0])

# users = [
#     ['vasia', 25],
#     ['dima', 45]
#     ['petia', 27,[
#         '232323',
#         '323232'
#     ]],
#     ['vasia', 25],
#     ['dima', 45]
#     ['petia', 27,[
#         '232323',
#         '323232'
#     ]]
# ]


# a = [1, 5, 3, 1, 6, 5, 1, 6, 7, 8, 'hello', 'python']
# c = ['aaa', 'ccc', 'bbb', 'aa']
# c.append('eee') # добавить в конец
# c.insert(2, 'rrr') # добавить со вставкой в определенное место
# print(c)

# print(a.count(1)) # посчитать количество
# print(5 in a) # есть ли значение в списке

# a.pop() # удаляет последний
# a.pop(3) # удаляет с индексом 3
# a.remove('hello') # удаляет по значению
# del a[1:3] # удалить нескоолько елементов
# print(a.index('python')) # ищет индекс по значению

# c.sort() # менякт список 
# e = sorted(c) # не меняет список - возвращает в перемменную
# print(c)
# print(e)

# a.reverse()
# print(a)
# print(a[::-1])

# a.clear() # очистка

