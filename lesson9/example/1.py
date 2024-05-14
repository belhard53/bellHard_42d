# # from time import time
# # import time



# def f1():
#     global b, a
#     # print('1'*30)
#     b = 5
#     a = 1
#     # print(111,locals())
#     print(b)
#     def f2():
#         # global b
#         nonlocal b
#         b = 4
#         print(b)
        
    
    
# b = 2
# f1()
# print(b)
# print(a)
# # print(globals())


# рекурсия
# n = 0
# def f1(text):
#     global n
#     n += 1
#     if text:
#         print(n, text)
#         f1(text[:-1])
#     return
    
# f1("Hello Python")


# список для сортировки
# [1,2,3,4,[1,23,5,6,[2,[3,4, [8,9,0],5],3,4]], 4,[3,3,5],56]

# lambda
# f1 = lambda x:x**2
# print(f1(5))

# l = [[1,2,9,[1]], [3,4,9,[9]], [3,4,10, [0]]]
# ld = [(1,2), ("q", "22")]

# функция для использования как key в sorted
# # def f1(item):
# #     return item[3][0]

# функция для использования как key в filter
# def f2(item):
#     if item[2]==9:
#         return True
#     return False # else писать не обязательно т.к. тут без вариантов

# для key используется lambda или функции выше
# l2 = sorted(l, key=lambda x:x[3][0], reverse=True)
# l3 = list(filter(lambda x:True if x[2]==9 else False, l))
# print(l2)
# print(l3)

# users = [
#     {'name':'vasia', 
#         'surname':'vasiapupkin', 
#         'phone':'3752323232'},
#     {'name':'DIma', 
#      'surname':'DimaKrivenyz', 
#      'phone':'3752323232'},
#     {'name':'Petia', 
#      'surname':'DimaKrivenyz', 
#      'phone':'3752323232'}
# ]

# users2 = filter(lambda x:True if x['name']=='DIma' else False, users)
# print(list(users2))



# d = {1:11, 9:22, 3:33, 4:77, 7:44}
# print(d.items())
# d2 = dict(sorted(d.items(), key=lambda item:item[0])) # сортировка по ключу
# d3 = dict(sorted(d.items(), key=lambda item:item[1])) # сортировка по значению
# print(d2)
# print(d3)


