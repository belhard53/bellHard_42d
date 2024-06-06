from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# from sqlalchemy.orm import sessionmaker

from models import Quiz, Question, db_add_new_data
# from models import * 

sqlite_database = "sqlite:///lesson15\\example\\quiz.db"
engine = create_engine(sqlite_database, echo=False)

# Session = sessionmaker(autoflush=False, bind=engine) # как один из вариантов создания сессии

with Session(autoflush=False, bind=engine) as db:
    db_add_new_data(engine, db)

    qs = db.query(Quiz).all()
    print(1, qs)
    
    for q in qs:
        print(2, q)
    
    for question in qs[1].question:
        print(3, question)
    
    # q = db.query(Quiz).get(2)
    # print(2, q, q.question[1])
    
    # quests = db.query(Question).all()
    # for q in quests:
    #     print(q, q.quiz)
     
    # quests = db.query(Question).filter_by(id=1).one()
    # print(1111, quests)
    
    # quests = db.query(Question).filter(Question.id>6).all()
    # for q in quests:
    #     print(222, q, q.quiz)
    
    
    # from sqlalchemy import or_
    # db.users.filter(or_(db.users.name=='Ryan', db.users.country=='England'))
    
    
           
        
    # quests = db.query(Question).filter(Question.question.like('%море%')).all()
    # for q in quests:
    #     print(222, q, q.quiz)


    # ОБНОВЛЕНИЕ 
    # quiz = db.query(Quiz).get(1) # устарело - использовалось до 2.0
    # quiz = db.get(Quiz, 1)
    # quiz.name = "Новое название Квиза"
    # quiz.question[1].answer = 'Новый правильный ответ'    
    # db.commit()
    
    # quiz = db.query(Quiz).all()[0]
    # print(quiz.name)
    # print(*[f'{q.question} - {q.answer} \n' for q in quiz.question ]) # проверяем - все ок - обновилось
    
    
    # # УДАЛЕНИЕ    
    # quiz = db.get(Quiz, 1)
    # db.delete(quiz)
    # db.commit()
    # quizes = db.query(Quiz).all()
    # print(quizes)
    
    
    #pydantic 
    from schema import *
    json_question = """
    {
        "question":"name1",
        "answer":"answer1",
        "wrong1":"wrong11",
        "wrong2":"wrong22",
        "wrong3":"wrong33"
    }
    """

    q = QuestionSchema.parse_raw(json_question)
    print(q)
    print(q.dict())
    question = Question(**q.dict())
    print(question)