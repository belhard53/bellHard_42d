# import random # создается отдельное пространство имен random
# print(random.randint(1,10))
# import random as rnd # создается отдельное пространство имен rnd
# print(rnd.randint(1,10))
# from random import * # все в глобальное пространство имен
# print(randint(1, 10))



# import hero1
# from hero1 import Spell, Mag
# hero = hero3 = Mag('Gendalf', 30, 25, 10, 30, [])    

# from add_files2 import hero3
# hero = hero3.Hero('Dimitri', 50, 20, 15)   

# from add_files2.hero3 import Spell
# spell = Spell('spell1')

# from add_files1 import * # только Spell и Mag - так указано в __init__.py
# a = Spell('dd')

# if __name__  == '__main__':
#     print(__name__)

    
# import sys
# # sis.exit()
# # print(sys.path)
# a = sys.argv # аргументы к запуску файла

# import os
# p = os.getcwd()
# print(os.path.exists(p)) # есть ли файл
# print(os.listdir())
# pp = os.path.join(p, 'fold1', 'fold2', 'file1.jpg') # соединить путь
# print(pp)
# os.path.


# from pathlib import Path
# path = Path().home()
# path = Path(path, 'fold1', '111.jpg')
# print(111, path)
# print(222, path.parent.parent)
# for p in path.parents:
#     print(333, p)
    
# path = Path().cwd()
# # for p in path.iterdir():
# for p in path.glob('**/*'):
#     print(444, 'file' if p.is_file() else 'dir',  p )


            


# import math #математика
# math.sqrt(9)

# import copy
# # copy.deepcopy()

# import itertools
# itertools.count(start=0, step=1) #бесконечная арифметическая прогрессия с первым членом start и шагом step.
# itertools.cycle(iterable) #- возвращает по одному значению из последовательности, повторенной бесконечное число раз.
# itertools.repeat(elem, n=Inf) - повторяет elem n раз.
# itertools.accumulate(iterable) - аккумулирует суммы.
# ....


# import decimal
# print(0.1 + 0.1 + 0.1)

# import time
# t1 = time.time() # в секундах
# t2 = time.localtime() # в struct_time
# t3 = time.gmtime(30) # преобразует секунды в struct_time
# print(000, t3)
# print(111, t2.tm_yday, t2.tm_year)
# print(222, f'{time.ctime(t1)}') # преобразует в Oct 14 00:24:54 2023
# print(333, f'{time.gmtime(t1)}') # преобразует в struct_time
# print(444, time.strftime(r"%Y/%m/%d %H:%M:%S"))
# print(555, time.strftime(r"%Y/%m/%d %H:%M:%S", t2))
# print(666, time.strptime("11 55","%S %M"))

# # datetime
# # 	date — хранит дату
# # 	time — хранит время
# # 	datetime — хранит дату и время

# from datetime import datetime as dt
# from datetime import time as t
# from datetime import date as d

# timestamp = 1528797322
# date_time = dt.fromtimestamp(timestamp)

# current_date_time = dt.now()
# current_date = d.today()
# curent_time = t.isoformat
# print(current_date_time.day, current_date_time.hour)
# print(current_date_time, "/", 
#       current_date, '/', 
#       current_date_time.time())
# print(f"Текущее время {current_date_time:%d.%m.%Y %H:%M}")
# #Текущее время 24.02.2017 15:51

# date1 = d(2023,1,15)
# d_txt = date1.strftime("%d")
# print(d_txt)
# print(current_date_time.strftime(r"%d-%m/%Y %H-%M:%S"))
# print(f"{date1.day}.{date1.month}.{date1.year}")
# print(f"{current_date_time.day}.{current_date_time.month}.{current_date_time.year}")

# date_object = dt.strptime("22/11/2022", r"%d/%m/%Y")
# print(date_object, date_object.month)

# # timedelta - хранит какое-то время которое можно прибавить или отнять
# from datetime import timedelta
# time_add = timedelta(days=365)
# current_date_time += time_add
# print(current_date_time)

# # разница в датах
# d1 = dt.strptime("01.02.2017", "%d.%m.%Y")
# d2 = dt.strptime("01.03.2017 2", "%d.%m.%Y %H")
# d3 = dt.now()
# delta = d2 - d1
# delta2 = d3 - d1
# print( delta2, "/", delta2.days, "/",  
#             delta2.seconds, "/", delta2.total_seconds())


# from enum import Enum
# class CatColor(Enum):
#   WHITE = 0
#   BLACK = 1
#   GINGER = 2
  
# cat = CatColor.GINGER 

# # Выводит 2
# print(cat.value)
# # Выводит GINGER 
# print(cat.name)



# import logging    

# logging.basicConfig(level=logging.DEBUG, filename='111.log',
#                 format='%(asctime)s - %(levelname)s - %(message)s')


# logging.debug('111')
# logging.info('222')
# logging.warning('333')
# logging.error('444')
# logging.critical('55')



# try:
#     a=1/0
# except:
#     logging.error('555', exc_info=True)
# print(6)




# import re

# match - только с начала строки .group(0)
# search - везде - возвращает только 1
# findall - список всего
# split - разделить 
# sub - замена 

s = '3752912345678'
res = re.search(r'\+*375(29|33|44)[0-9]{7}', s)

if res:
	print(res[0])
	print(res.group(0))


# '^\w+' - первое слово
# '^[a-zA-Z][a-zA-Z0-9-_\.]{1,20}$' - логин
# '(\+375)(29|33|44)[0-9]{7}' - телефон
# '\d\d\/\d\d\/\d{4}' - дата
# '[-+]?\d+' = любая цифра но с + или с -

