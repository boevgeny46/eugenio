import sqlite3

# подключаемся к нашей базе данных
connection = sqlite3.connect('films_db.sqlite')

# оздаем курсор и через курсор созаем запросы
cursor = connection.cursor()

# запрос по доставке информации  fetchall команда доставить все запрошенные по запросу элементы
# fetchone- доставит только первый элемент
#  fetchmany(N) - выдаст только N первых элементов
result = cursor.execute("""SELECT * FROM films WHERE year =? and duration > ?""", (2010, 90)).fetchall()

# вывод информации на экран:
for item in result:
    print(item)
# отключаемся от базы данных (disconnect)
connection.close()

# программа работает
#   rrr