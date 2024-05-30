import  sqlite3


con = sqlite3.connect('lesson14\\222.db')
cur = con.cursor()

# cur.execute("INSERT INTO ttt1 VALUES (?,?,?)",('19','101010','4'))
# con.commit()  # если без with нужно обязательно писать commit для сохранения

newTable = """CREATE TABLE IF NOT EXISTS ttt1(
               userid INTEGER PRIMARY KEY AUTOINCREMENT,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """
cur.execute(newTable)
con.commit()


with con:
    newData = [('1','ffff1','llll1','m'),
               ('2','ffff2','llll2','m'),
               ('3','ffff3','llll3','f'),
               ('4','ffff4','llll4','m')]
    cur.execute('DELETE FROM ttt1')
    cur.executemany("INSERT INTO ttt1 VALUES(?,?,?,?)",newData)


with con:
    print(cur.execute('SELECT * FROM ttt1').fetchall()) #все
    print (cur.execute('SELECT * FROM ttt1').fetchall()[0]) #первая запись
    print(len(cur.execute('SELECT * FROM ttt1').fetchall())) # количество строк в курсоре
    # print(cur.execute('SELECT * FROM ttt1 WHERE id = ? ',('1')).fetchall())
    #print(cur.execute("INSERT INTO ttt1 ('id', 'user_id','user_type') VALUES (?,?,?)",('17','8888','4')).lastrowid)  # вставка и возврат id


print('------------')
with con:
    print(cur.execute('SELECT * FROM ttt1 WHERE true').fetchone()) 
    print(cur.execute('SELECT * FROM ttt1 WHERE true').fetchmany(3))