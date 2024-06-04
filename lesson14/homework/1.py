"""
Используя класс из пред.урока обеспечить хранение и сохранение любых изменений в базе 
данных. Для этого можно к примеру добавить в класс метод save который будет сохранять или 
создавать пользователя в базе данных и использовать его при любых изменениях.


* в базе данных создать таблицу предоставляемых услуг со след полями
	название
	тип (1 - платная 0 - бесплатная)
	стоимость 
	период в днях
** в класс пользователя добавить методы:
	добавить услугу (услуг у одного пользователя может быть несколько)
	продлить услугу (продлить можно если услуга еще не закончена, иначе добавить)
	удалить услугу
*** создать консольное или оконное приложение которое показывает меню и отрабатывает выбранный пункт.
	Меню:
		1 - показать пользователей
		2 - информация о пользователе (в т.ч. и подключенные услуги)
		3 - список услуг		
		4 - показать пользователей с определенной услугой
		5 - показать пользователей у которых за прошедший месяц окончился период хоть одной услуги 
 
	
 
"""

# ВАРИАНТ ОДНОГО ИЗ УЧЕНИКОВ


import re
import datetime
import random
import sqlite3

db_name = 'user.db'
conn = None
cursor = None
 
def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
 
def close():
    cursor.close()
    conn.close()
 
def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    do('''CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY, 
            name VARCHAR,
            login VARCHAR, 
            password VARCHAR, 
            subscription_mode VARCHAR, 
            subscription_date VARCHAR, 
            is_blocked bit)''' 
    )
    close()

class User():
    __password = ''
     
    def __init__(self, name, login, password="") -> None:
        if not password:
            password=self.genpass()
            print(f"New generated password - {password}")
        self.name = name
        self.login = login
        self.password = password
        self.subscription_mode='free'
        self.subscription_date=datetime.date.today()+datetime.timedelta(days=30)
        self.is_blocked=False
        self.insert()
    
    def bloc(self, blocked):
        self.is_blocked=blocked
        self.update()

    def check_subscr(self, datesub=0):
        subb=False
        if not datesub:
            datesub=datetime.date.today()
        else:
            datesub= datetime.datetime.strptime(datesub, "%Y-%m-%d").date()
        subb= self.subscription_date> datesub
        return (subb, self.subscription_mode, (self.subscription_date - datesub).days)
            
    def genpass(self):
        chars1 = 'abcdefghijklnopqrstuvwxyz'
        chars2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars3 = '1234567890'
        passw =''
        for i in range(2):
            passw += random.choice(chars1)
            passw += random.choice(chars2)
            passw += random.choice(chars3)
        return passw

    def change_pass(self, passw=0):
        if not passw:
            passw=self.genpass()
            print(f"New generated password - {passw}")
        self.password=passw
        self.update()

    def get_info(self):
        print(f"User name-{self.name}")
        print(f"User login-{self.login}")
        print(f"User subscription_mode-{self.subscription_mode}")
        print(f"User subscription_date-{self.subscription_date}")
        if self.is_blocked:
            print(f"User blocked")

    def insert(self):
        open()
        cursor.execute('''PRAGMA foreign_keys=on''')
        query = f"""
            INSERT INTO user 
                (name ,login, password, subscription_mode, subscription_date, is_blocked) 
            VALUES 
                ('{self.name}','{self.login}','{self.password}','{self.subscription_mode}', 
                                        '{self.subscription_date}',{self.is_blocked})
            """
        print(query)
        cursor.execute(query)
        conn.commit()        
        close()
        print("insert")

    def update(self):
        open()
        cursor.execute('''PRAGMA foreign_keys=on''')
        query = f"""
            UPDATE user 
            SET name='{self.name}',
                login='{self.login}', 
                password='{self.password}', 
                subscription_mode='{self.subscription_mode}', 
                subscription_date='{self.subscription_date}', 
                is_blocked={self.is_blocked} 
            WHERE login='{self.login}'"""
        print(query)
        cursor.execute(query)
        conn.commit()        
        close()
        print("update")
 
    @property #getter  
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val):
        res = re.search(r'[a-zA-Z0-9-_]{6,}$', val)
        if res:    
            self.__password=val
        else:
            raise ValueError("Password not valid")
      
            
create()
#user = User('Vasia','vasia1999','dvejnvnju&&98')
user = User('Vasia','vasia1999')

user.get_info()
user.change_pass("Dddd_jj") # нету цифр но проходит
print(user.password)
#print(user.check_subscr('2024-07-01'))
print(user.check_subscr('2024-08-01'))


