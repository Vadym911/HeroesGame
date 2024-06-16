
import sqlite3

def db_create_connect():
    database = sqlite3.connect("books.db")
    database.close()

def db_create_table():
    database = sqlite3.connect("books.db")

    cursor = database.cursor()
    cursor.execute('''CREATE TABLE books(
    article TEXT,
    authot TEXT,
    reviews INTEGER)
    ''')

    database.commit()
    database.close()


def db_insert():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("INSERT INTO books VALUES('Про користь тараканів', 'Андрій Безуглий', 1001)")
    cursor.execute("INSERT INTO books VALUES('Про користь розведення корів в квартирі', 'Максим Жулинський', 2500)")
    cursor.execute("INSERT INTO books VALUES('Лікувальний ефект козявок з носу', 'Юрій Погребняк', 3500)")
    cursor.execute("INSERT INTO books VALUES('Пригоди простроченної ковбаси в нашому тілі', 'Влад Ткач', 569)")
    cursor.execute("INSERT INTO books VALUES('Пласка земля - в пошуках трьох слонів і черепахи', 'Єгор Калашніков', 100500)")


    database.commit()
    database.close()

def db_fetch():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    print(data)

    print("-"*20)

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchone()
    print(data)

    print("-" * 20)

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchmany(2)
    print(data)


    database.close()

def db_select():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("SELECT article FROM books")
    data = cursor.fetchall()
    print(data)

    print("-" * 20)

    cursor.execute("SELECT authot FROM books")
    data = cursor.fetchall()
    print(data)

    print("-" * 20)

    cursor.execute("SELECT rowid, article FROM books")
    data = cursor.fetchall()
    print(data)

    print("-" * 20)

    cursor.execute("SELECT rowid, * FROM books")
    data = cursor.fetchall()
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    database.close()


def db_where():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("SELECT rowid, * FROM books WHERE reviews > 3000")
    data = cursor.fetchall()
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    print("-"*20)

    cursor.execute("SELECT rowid, * FROM books WHERE authot <> 'Максим Жулинський'")
    data = cursor.fetchall()
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    cursor.execute("SELECT rowid, * FROM books WHERE reviews < 2000")
    data = cursor.fetchall()
    print("Список непопуярних книг")
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    database.close()

db_where()

print("-"*20)
def db_sorting():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("SELECT rowid, * FROM books ORDER BY authot ASC")
    data = cursor.fetchall()
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    print("-" * 20)

    cursor.execute("SELECT rowid, * FROM books ORDER BY authot DESC")
    data = cursor.fetchall()
    for book in data:
        print(f"{book[0]}. Книга {book[1]}, автор - {book[2]}, переглядів - {book[3]}")

    database.close()




def db_update():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("UPDATE books SET authot = 'Ivan Shamrykov' WHERE articles = 'Лікувальний ефект козявок з носу'")
    cursor.execute("UPDATE books SET reviews = 100500 WHERE rowid > 1")

    database.commit()
    database.close()


def db_delete():
    database = sqlite3.connect("books.db")
    cursor = database.cursor()

    cursor.execute("DELETE FROM books WHERE reviews < 2000")

    database.commit()
    database.close()

def db():
    pass