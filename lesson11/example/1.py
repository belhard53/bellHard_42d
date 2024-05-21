class Hero:
    """     
    Класс дял создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """
    #  свойства класса - каждый созданный объект будет их иметь по умолчанию
    option1 = True
    points = 0
    level = 1

    # конструктор - тут мы создаем свойства которые должны быть у каждого нового объекта
    # и присылаем сюда первоначальные их значения
    def __init__(self, name, health, armor, strong) -> None:
        # свойства объектов
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    # методы - это действия/команды которые могут выполнять объекты
    def print_info(self):
        print(
              f"Имя {self.name}\n" \
              f"Здоровье - {self.health}\n" \
              f"Защита {self.armor}\n"
        )
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
            
        

hero1 = Hero('Dimitri', 50, 20, 15)    
hero2 = Hero('Alex', 60, 10, 5)    
hero3 = Hero('Yuri', 30, 25, 10)    



hero2.print_info()
hero1.kick(hero2)
hero2.print_info()
hero1.kick(hero2)
hero2.print_info()