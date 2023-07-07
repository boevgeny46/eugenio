import sqlite3

# # подключаемся к нашей базе данных
# connection = sqlite3.connect('films_db.sqlite')
#
# # оздаем курсор и через курсор созаем запросы
# cursor = connection.cursor()
#
# # запрос по доставке информации  fetchall команда доставить все запрошенные по запросу элементы
# # fetchone- доставит только первый элемент
# #  fetchmany(N) - выдаст только N первых элементов
# result = cursor.execute("""SELECT * FROM films WHERE year =? and duration > ?""", (2010, 90)).fetchall()
#
# # вывод информации на экран:
# for item in result:
#     print(item)
# # отключаемся от базы данных (disconnect)
# connection.close()
#
# # программа работает
#   rrr


import sqlite3

# подключаемся к нашей базе данных ли создаем новую базу данных
connection = sqlite3.connect('shop.sqlite')

# оздаем курсор и через курсор созаем запросы
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
userid INT PRIMARY KEY, fname TEXT, lname TEXT, gender TEXT);""")

cursor.execute("""CREATE TABLE IF NOT EXISTS orders(
orderid INT PRIMARY KEY, date TEXT, userid INT, total INT);""")
#
# cursor.execute("""INSERT INTO users(
# userid, fname,lname, gender)VALUES(1,'Alex,'Smith', 'male')""")



connection.commit()

# запрос по доставке информации  fetchall команда доставить все запрошенные по запросу элементы
# fetchone- доставит только первый элемент
#  fetchmany(N) - выдаст только N первых элементов
#result = cursor.execute("""SELECT * FROM films WHERE year =? and duration > ?""", (2010, 90)).fetchall()

# вывод информации на экран:
#for item in result:
#    print(item)
# отключаемся от базы данных (disconnect)
connection.close()



