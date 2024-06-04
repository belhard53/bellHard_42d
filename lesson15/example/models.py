from sqlalchemy import (Column, ForeignKey, Table,
                        Integer, String, Text, Boolean, Date, DateTime)

from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    ...
    
    
class User(Base):
    __tablename__ = 'user'
    # __table_args__ = (CheckConstraint("char_length(name) >= 4"),)
    
    id = Column(Integer, primary_key=True)
    name = Column(String(25))    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())   
    quizes = relationship('Quiz', backref='user')
    
    
        
        
     
class Quiz(Base):    
    __tablename__ = 'quiz'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())   
    
    def __init__(self, name:str, user:User) -> None:
        super().__init__()
        self.name = name
        self.user = user
        
    def __repr__(self):
        return self.name

quiz_question = Table(
            'quiz_question',
            Base.metadata,
            Column('quiz_id', Integer, ForeignKey('quiz.id')),
            Column('question_id', Integer, ForeignKey('question.id')),
            )


class Question(Base):    
    __tablename__ = 'question'
    
    id = Column(Integer(), primary_key=True)
    question = Column(String(250), nullable=False)
    answer = Column(String(100), nullable=False)
    wrong1 = Column(String(100), nullable=False)
    wrong2 = Column(String(100), nullable=False)
    wrong3 = Column(String(100), nullable=False)
    quiz = relationship('Quiz', 
                           secondary=quiz_question,
                           backref = 'question')   

    def __init__(self, question, answer, wrong1, wrong2, wrong3) -> None:
        super().__init__()
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        
    def __repr__(self):
        return self.question


def db_add_new_data(engine, db):
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    users = [
            User(name='User1'), 
            User(name='User2'),
            User(name='User3')
    ]
    
    
    quiz1 = Quiz(name='Опрос N1', user=users[0])
    quiz2 = Quiz('Опрос N2', users[1])
    quiz_list:list = [
        Quiz('Опрос N3', users[1]), 
        Quiz('Опрос N4', users[1])
    ]

    question = Question('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два')
    question_list = [
        Question('Каким станет зелёный утёс, если упадет в Красное море?', 'Мокрым?', 'Красным', 'Не изменится', 'Фиолетовым'),
        Question('Каким станет зелёный утёс, если упадет в Красное море?', 'Мокрым?', 'Красным', 'Не изменится', 'Фиолетовым'),
        Question('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        Question('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        Question('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        Question('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако'),
        Question('Что такое у меня в кармашке?', 'Кольцо', 'Кулак', 'Дырка', 'Бублик')
    ]
    
    quiz1.question.append(question)
    quiz1.question.append(question_list[0])
    quiz1.question.append(question_list[1])
    quiz1.question.append(question_list[2])

    quiz2.question.append(question)
    quiz2.question.append(question_list[3])
    quiz2.question.append(question_list[4])
    quiz2.question.append(question_list[5])

    
    quiz_list[0].question.append(question_list[6])
    quiz_list[0].question.append(question_list[5])
    quiz_list[0].question.append(question_list[4])
    quiz_list[0].question.append(question_list[3])
    
    
    # добавляем пользователей а вместе с ними добавятся все связанные с ними записи из др.таблиц
    db.add_all(users) 
    
    db.commit()

