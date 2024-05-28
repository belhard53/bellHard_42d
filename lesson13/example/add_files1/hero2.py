class Spell:
    def __init__(self, name, dang=10, mana=5, type=1) -> None:
        self.name = name

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
    def _get_info(self):
        print(
              f"Имя {self.name}\n" \
              f"Здоровье - {self.health}\n" \
              f"Защита {self.armor}"
        )
        
    def print_info(self):
        
        print(self._get_info() + '\n')
    
    def kick(self, other):        
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0
            

class Mag(Hero):    
    def __init__(self, name, health, armor, strong, mana, spells) -> None:
        # Hero.__init__(self, name, health, armor, strong)
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.spells = spells
        self.base_spell = fireball
        


    def cast_spell(self):
        print(self.base_spell)
    

    def print_info(self, sep="-"):
        info =  f"{super()._get_info()}\n"  \
                f"{sep*20}\n" \
                f"Мана - {self.mana}\n"
        print(info)


class Knight(Hero):
    def __init__(self, name, health, armor, strong ) -> None:
        super().__init__(name, health, armor, strong)


