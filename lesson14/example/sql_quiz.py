# файл где изучение форм
import sqlite3
from random import randint
 
db_name = 'lesson14\\quiz.db'
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
 
def clear_db():
    ''' убивает все таблицы '''
    open()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    close()
 
def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    do('''CREATE TABLE IF NOT EXISTS quiz (
            id INTEGER PRIMARY KEY, 
            name VARCHAR)''' 
    )
    do('''CREATE TABLE IF NOT EXISTS question (
                id INTEGER PRIMARY KEY, 
                question VARCHAR, 
                answer VARCHAR, 
                wrong1 VARCHAR, 
                wrong2 VARCHAR, 
                wrong3 VARCHAR)'''
    )
    do('''CREATE TABLE IF NOT EXISTS quiz_content (
                id INTEGER PRIMARY KEY,
                quiz_id INTEGER,
                question_id INTEGER,
                FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                FOREIGN KEY (question_id) REFERENCES question (id) )'''
    )
    close()
 
def show(table):
    #"SELECT id, name FROM quiz WHERE name LIKE 'Виктори%'"
    #"SELECT name FROM quiz WHERE name = 'Викторина 1'"
    # * - все столбцы
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    # [(1, 'Викторина1'), (1, 'Викторина1')]
    close()
 
def show_tables():
    show('question')
    show('quiz')
    show('quiz_content')
 
def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Каким станет зелёный утёс, если упадет в Красное море?', 'Мокрым?', 'Красным', 'Не изменится', 'Фиолетовым'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой', 'Левой', 'Любой'),
        ('Что не имеет длины, глубины, ширины, высоты, а можно измерить?', 'Время', 'Глупость', 'Море', 'Воздух'),
        ('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы', 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Парашют', 'Облако'),
        ('Что такое у меня в кармашке?', 'Кольцо', 'Кулак', 'Дырка', 'Бублик')
    ]
    open()
    cursor.executemany('''INSERT INTO question (question, answer, wrong1, wrong2, wrong3) VALUES (?,?,?,?,?)''', questions)
    conn.commit()
    close()
 
def add_quiz():
    quizes = [
        ('Викторина 1', ),
        ('Викторина 2', ),
        ('Викторина-непоймикакая', )
    ]
    open()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()
 
def add_links():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = """INSERT INTO quiz_content 
        (quiz_id, question_id) 
        VALUES (?,?)"""
    #answer = input("Добавить связь (y / n)?")
    links = [
        (1,1), (1,2), (1,4), (1,6), 
        (2,2), (2,5), (2,3), (2,1), 
        (3,3), (3,6), (3,5), (3,2)
    ]

    for link in links:
        quiz_id = link[0]
        question_id = link[1]
        cursor.execute(query, [quiz_id, question_id])
    
    conn.commit()        
    close()
 
def get_question_after(last_id=0, vict_id=1):
    ''' возвращает следующий вопрос после вопроса с переданным id
    для первого вопроса передаётся значение по умолчанию '''
    open()
    query = '''
    SELECT quiz_content.id, question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content 
    WHERE quiz_content.question_id == question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id == ? 
    ORDER BY quiz_content.id '''
    cursor.execute(query, [last_id, vict_id] )
 
    result = cursor.fetchone()
    close()
    return result 
 
def get_quises():
    ''' возвращает список викторин (id, name) 
    можно брать только викторины, в которых есть вопросы, но пока простой вариант '''
    query = 'SELECT * FROM quiz ORDER BY id'
    open()
    cursor.execute(query)
    result = cursor.fetchall()
    close()    
    return result
 
def get_quiz_count():
    ''' необязательная функция '''
    query = 'SELECT MAX(quiz_id) FROM quiz_content'
    open()
    cursor.execute(query)
    result = cursor.fetchone()
    close()
    return result
    
 
def get_random_quiz_id():
    query = 'SELECT quiz_id FROM quiz_content'
    open()
    cursor.execute(query)
    ids = cursor.fetchall()
    rand_num = randint(0, len(ids) - 1)
    rand_id = ids[rand_num][0]
    close()
    return rand_id

def get_quiz(quiz_id):
    open()
    query = '''
    SELECT question.question, question.answer, question.wrong1, question.wrong2, question.wrong3
    FROM quiz_content
    LEFT  JOIN question ON quiz_content.question_id = question.id 
    WHERE quiz_content.quiz_id = ?
    ORDER BY quiz_content.id '''
    cursor.execute(query, [quiz_id])
    result = cursor.fetchall()        
    close()
    return result

def check_answer(q_id, ans_text):
    query = '''
            SELECT question.answer 
            FROM quiz_content, question 
            WHERE quiz_content.id = (?) 
            AND quiz_content.question_id = question.id
        '''
    open()    
    cursor.execute(query, [str(q_id)])
    result = cursor.fetchone()
    close()    
    # print(result)
    if result is None:
        return False # не нашли
    else:
        if result[0] == ans_text:
            # print(ans_text)
            return True # ответ совпал
        else:
            return False # нашли, но ответ не совпал
 
def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    show_tables()
    add_links()
    show_tables()
    # print(get_question_after(0, 3))
    # print(get_quiz_count())
    # print(get_random_quiz_id())
    
    # Вывод в консоль вопросов квиза номер 2
    print("\n Квиз 2")
    res = get_quiz(2)
    if res:
        for row in res:
            print(row)

    # Вывод в консоль вопроса с id=3, id викторины = 1
    print("\n Квиз 1 вопрос 2")
    print(get_question_after(3, 1))
    
if __name__ == "__main__":
    # main()
    # print(get_quises())
    print(get_quiz(1))


# "UPDATE quiz SET name ='Викторина 4' WHERE id = 3"
# "UPDATE quiz SET name ='Викторина 4' WHERE name ='Викторина 3'"
# "DELETE FROM quiz WHERE id = 3"
# "DELETE FROM quiz WHERE name LIKE '% old %'"