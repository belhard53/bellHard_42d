class User:
    
    tablename = "user"
    
    # статический метод - внутренний метод который выполняется как правило внутри класса
    # для "служебных" нужд - сюда не передается self
    @staticmethod
    def multiply(a, b):
        return a * b
    
    # метод класса - сюда передается не self a cls - сам объект класса
    # например чтобы поменять значение атрибутов(свойств) класса
    @classmethod
    def change_tablename(cls, new_tablename):
        cls.tablename = new_tablename
    
    
    def __init__(self, name, login, age) -> None:
        self.name = name
        self.login = login
        self.age = age
        self.projects = []
        
    # след методы определяют каким образом будут сравниваться объекты
    # равны ли - obj1 == obj2
    def __eq__(self, other) -> bool:
        return self.age == other.age
    
    # меньше  ли - obj1 < obj2
    def __lt__(self, other) -> bool:
        return self.age < other.age
    # аналогично
    # __ne__(self, other)   obj1 != obj2
    # __le__(self, other)   obj1 <= obj2
    # __gt__(self, other)   obj1 >  obj2
    # __ge__(self, other)   obj1 >= obj2

    
    
    def __str__(self) -> str:
        # return f"{self.name} - {self.age}, логин -  {self.login}"
        return f"{self.name} - {self.age}"
    
    def __repr__(self) -> str:
        return f"User({self.name}, {self.age})"
    
    
    # len как и некоторые др. маг.методы по подсказке не выдаются но работают    
    def __len__(self):
        return len(self.name) + len(self.login)
    
    def __call__(self):
        print("Класс User")
    
    def get_proj(self, n):
        return self.projects[n]
    
    def add_proj(self, proj_name:str):
        self.projects.append(proj_name)

class Users:
    users = []
    num = 0
    
    def __str__(self):                
        return "\n".join([str(user) for user in self.users])
    
    def __len__(self):
        return len(self.users)
    
    def __setitem__(self, key, value):
        self.users[key] = value
    
    def __getitem__(self, key:int):        
        return self.users[key]
    
    def __delitem__(self, key, value):
        pass
    
    def __iter__(self):
        return iter(self.users)
    
    def __next__(self):
        res =  self.users[n]
        n+=1
        return res
    
    def add(self, user:User):
        self.users.append(user)
        
User.tablename = "admin"     
        
user1 = User('vasia', 'vvv123', 33)
user2 = User('Petia', 'ppp123', 22)
user3 = User('Tania', 'ttt123', 22)
users = Users()

user1.add_proj('Calculator')
user1.add_proj('Memo_pad')

# User.tablename  =
user1.__class__.tablename = "admin"

print(user2 == user3) # -> True

print(len(user1))

setattr(user1, 'age', 44)
user1.password = "123"
print(user1.password)
setattr(user2, 'password', '321')
print(user1.__dict__)

users.add(user1)
users.add(user2)

print(users)
print(users[1])


