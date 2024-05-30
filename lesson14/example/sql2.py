import sqlite3


con = sqlite3.connect('d:/testBase5.db')
cur = con.cursor()

newTable = """CREATE TABLE IF NOT EXISTS users2(
               userid INTEGER PRIMARY KEY AUTOINCREMENT,
               fname TEXT,
               lname TEXT,
               gender TEXT);
            """
cur.execute(newTable)
con.commit()

sql = "INSERT INTO users (name, login, password, phone, sub_date) " \
      "VALUES ('Dmitry', 'DimaBig', 'dima1234', '7854145', '12.11.2021')"

sql = "SELECT * FROM users WHERE name = 'uuu2'"

# sql = "UPDATE users SET password = 'qqqqq' WHERE name = 'uuu2' AND login = 'lll'"

# sql =  "DELETE FROM users WHERE name = 'uuu2' AND login = 'lll'"

with con:
    q = cur.execute(sql)
print(len(q))