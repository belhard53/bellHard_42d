# for - когда знаем сколько раз повторить, или что то перебрать
# while - когда не знаем сколько повторов

# import time
# from random import randint

# a = 0 
# b = 1
# i = 1
# rain = False
# # пока правда - я делаю
# while a < 20 and b < 3:
#     a += 1
#     if a%3 == 0:
#         continue # пропускает все строки до конца цикла
        
#     print(a)
    
#     r = randint(1,50)
#     if r == 1:
#         rain = True
#     # time.sleep(1)
#     if rain:
#         break # останавливает цикл

# print("Все")

    
# menu = '''
# 1 - djsldj
# 2 - 2dsdsd
# 3 - dsdsds
# 0 / exit - выход

# '''    

# программа без остановки    
# a = input(menu")
# while a != '0' and a != 'exit':
#     if a == "1":
#         print(111)
#     elif a == "2":
#         print(222)
#     elif a == "3":
#         print(333)
#     else:
#         print('Нет такой команды')        
#     a = input(menu)
    
    
# s = list(range(10)) # список от 0 до 10 (10 - не включено)
# print(s)

# for i in [1,2,3,4,5,6,7,8]:
#     print(i)
#     print(i*2)
#     print(i**2)
#     print(i**i)


# for i in range(3): #  цикл на 3 повторения
#     p = input('password')
#     if p == "1234":
#         print(f'ok c попытки{i+1}')
#         break

# bad_symbols = "!@#$%^&*())"
# login = 'hello!d@sds'
# for symbol in login: # перебор строки
#     # print(symbol)
#     if symbol in bad_symbols:
#         print(f"Нельзя - {symbol}")
  
  
# user1 = {'FIO':'Ivanov', 'Dol':'Direktor', 'GodRozh':'1990', 'Navyki': 'First', 'Deti':[1,2,3,4]}
# user2 = {'FIO':'Petrov', 'Dol':'GlavBuh', 'GodRozh':'1995', 'Navyki': 'Second', 'Deti':[1,2,3,4]}
# user3 = {'FIO':'Sidorov', 'Dol':'Spec', 'GodRozh':'1993', 'Navyki': 'Third', 'Deti':[1,2,3,4]}
# users = [user1, user2, user3]  

# for key in user1: # перебор словаря по ключам
#     print(key, user1[key])
    
# print(user1.items())
# for key, val in user1.items(): # перебор слооваря по элементам
#     print(key, val)
#     if key == 'Deti':
#         for ch in val: 
#             print("   -", ch)

# u1, u2, u3 = users


# три последующих цикла делают одно и то же
# i = 1
# for user in users:
#     print(f"{i} - {user['FIO']}")
#     i += 1

# for i in range(len(users)):
#     print(f"{i+1} - {users[i]['FIO']}")
   
# for i, user in enumerate(users):
#     print(f"{i+1} - {user['FIO']}")




# for i1, i2, i3 in zip(s1, s2, s3): # цикл по нескольким спискам
#     pass
    

# for user in users:
#     if user['FIO'] == 'Ivanov':
#         print(user)
    

#a = 0
# while 1:
#     if a = 1:
#         break
    


# генераторы списков и словарей - List comprehension

# nums = [1,2,3,4,5,9,15,20,19]

# nums2 = []
# for num in nums:    
#     if num%2 == 0:
#         # c = num + 3
#         nums2.append(num + 3)
    
# делает тоже самое что и код выше
# nums3 = [num + 3 for num in nums if num%2 == 0]    

# print(nums2)
# print(nums3)

# # for num in [num + 3 for num in nums if num%2 == 0]:
# #     print(num, end = ", ")

# создаем словарь из списка
# d = {num+num:num**num for num in nums}
# print(d)

# d = {input("Имя"):input("возраст") for _ in range(3)}
# print(d)
#---------------------------------

