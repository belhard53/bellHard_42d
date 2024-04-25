# ok = True
# ok = False
# print(type(ok))

# a = 1 + 1

# ok = 2 == 3
# ok = 2 > 3
# ok = 2 < 3
# ok = 2 <= 3
# ok = 2 >= 3
# ok = 2 != 3
# ok = not 2 == 2

# a = 0 - False
# a != 0 - True

# b = "a" True
# b = "" Flase
# b != "" True

# c = []
#if not c:
# if c:
#     pass

# if ok == True: # bad practics
# if ok:

# a < 3 
# a < 3 and a > 0
# a < 3 or a > 6

# a = 1 
# if a > 0:
#     print("a is positive")
# elif a == 0:
#     print("a is zero")
# else:
#     print("a is negative")


# a = 4
# b = 1
# if a == 1:
#     print(11)   
#     if b == 1:        
#         print(44)    
#         if 1:
#             print(66)
#     else:
#         print(55)
# elif a == 2:
#     print(22) 
# elif a == 3:
#     print(33)
# else:
#     print(000)    

# если не elif пришлось бы так писать 
# if a != 1 and a != 2 and a != 3:
#     print(000)




# ok = True and True - True
# ok = True and False - False

# ok = True or True - True
# ok = True or False - True

# ok = True or False or False - True
# ok = True or False and True - True
# ok = True or False and False - False
# ok = False or False or False - False

# ok = True and False or True - False
# ok = True and (False or True) - True - скобки вначале 



# user = ['name1', 'pass1','log1']
# user = []
# if user and user[1] == 'pass1':
#     print(1)

# b = 0    
# a = 1 if b == 0 else 2
# print(f"hello {1 if b == 1 else 2}")


# x = True
# y = False
# z = False
# if not x or y:
#     print(1)
# elif not x or not y and z:
#     print(2)
# elif not x or y or not y and x:
#     print(3)
# else:
#     print(4)



# a = 11
# if a % 2:
#     print("нечет")
# else:
#     print("чет")
    
# print('нечет' if a%2 else "чет")    



# a = 1 == 1
# #if isinstance(a, int | bool): # python 3.10+
# if isinstance(a, (int, bool)):
#     print('int or bool')

#all - все 
#any - любой
    
# if any([True, 0, 0, 0]):
#     print('ok')
    
# if all([1, 1, 1, 1]):
#     print('ok')
    
# a = None    
# if a:
#     print(1)
    
# b = a or 2   
# print(b)


# x=True
# print((1,2)[x])


# a = 1
# if a == 1 or a == 5 or a == 6:
#     print(11)
# elif a == 2 or a == 9:
#     print(22)
# elif a == 3:
#     print(33)
# elif a == 4:
#     print(33)


# match a:
#     case 1|5|6:
#         print(11)
#     case 2:
#         print(2)
#     case 3:
#         print(33)
        
# user = ['Vasia', 'log1', '123']   
# match user:
#     case name, 'admin1' | "admin2" as login, '123' | '1234' as pas:
#         print(f'ok - {name} {login}')
#     case name, login:
#         print("чеегото не хватает")
#     case _:
#         print('err')


# еще один вариант вывести на экран в зависимости от переменной
# com = {
#     1:"11",
#     2:"22",
#     3:"22",
#     4:"22"
# }
# a = 2
# print(com[a])

