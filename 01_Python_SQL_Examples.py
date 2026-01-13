import sqlite3
import os

def connect_database():
    if os.path.exists('01_Python_SQL_Examples.db'):
        os.remove('01_Python_SQL_Examples.db')

    conn = sqlite3.connect('01_Python_SQL_Examples.db')
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE Students(
        ID INTEGER PRIMARY KEY,
        NAME VARCHAR(255),
        AGE INTEGER,
        EMAIL VARCHAR(255),
        CITY VARCHAR(255)
    )
    ''')

    cursor.execute('''
   CREATE TABLE Courses(
       ID INTEGER PRIMARY KEY,
       COURSE VARCHAR(255),
       INSTRUCTOR VARCHAR(255),
       CREDIT INTEGER
   )
   ''')

def insert_data(cursor):
    students_data = [
        (1, 'Alice Johnson', 20, 'alice@gmail.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@gmail.com', 'Chicago'),
        (3, 'Carol White', 21, 'carol@gmail.com', 'Boston'),
        (4, 'David Brown', 20, 'david@gmail.com', 'New York'),
        (5, 'Emma Davis', 22, 'emma@gmail.com', 'Seattle')
    ]

    cursor.executemany("INSERT INTO Students VALUES (?,?,?,?,?)", students_data)

    courses_data = [
        (1, 'Python Programming', 'Dr. Anderson', 3),
        (2, 'Web Development', 'Prof. Wilson', 4),
        (3, 'Data Science', 'Dr. Taylor', 3),
        (4, 'Mobile Apps', 'Prof. Garcia', 2)
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?,?,?,?)", courses_data)

    print("Tables Created")

def basic_sql_operations(cursor):
    #1) SELECT ALL
    print("------SELECT ALL------")
    cursor.execute("SELECT * FROM Students")
    results = cursor.fetchall()
    for row in results:
        print(row)

    #2) SELECT COLUMNS
    print("------SELECT COLUMNS------")
    cursor.execute("SELECT name, age FROM Students")
    results = cursor.fetchall()
    for row in results:
        print(row)

    #3) WHERE QUERY
    print("------WHERE QUERY------")
    cursor.execute("SELECT * FROM Students WHERE age>20")
    results = cursor.fetchall()
    for row in results:
        print(row)

    #4) ORDER BY
    print("------ORDER BY QUERY------")
    cursor.execute("SELECT * FROM Students ORDER BY age")
    results = cursor.fetchall()
    for row in results:
        print(row)

def sql_insert_update_delete_operations(conn, cursor):
    # INSERT
    cursor.execute("INSERT INTO Students VALUES (6, 'Frank Miller', 23, 'frank@gmail.com','Miami')")
    conn.commit()

    #UPDATE
    cursor.execute("UPDATE Students SET age = 24 WHERE ID = 6")
    conn.commit()

    #DELETE
    cursor.execute("DELETE FROM Students WHERE ID = 6")
    conn.commit()

def aggregate_functions(cursor):
    #COUNT
    cursor.execute("SELECT COUNT(*) FROM Students WHERE age > 20")
    result = cursor.fetchone()
    print(result[0])

    #AVG
    cursor.execute("SELECT AVG(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    #SUM
    cursor.execute("SELECT SUM(age) FROM Students")
    result = cursor.fetchone()
    print(result[0])

    #MAX-MIN
    cursor.execute("SELECT MAX(age), MIN(age) FROM Students")
    result = cursor.fetchone()
    print(f"Max: {result[0]}, Min: {result[1]}")

def questions_and_answers(cursor):
    # SIMPLE
    print("SIMPLE QUESTIONS")
    print("1) Bütün kursların bilgilerini getirin")
    cursor.execute("SELECT * FROM Courses")
    for row in cursor.fetchall():
        print(row)

    print("2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin")
    cursor.execute("SELECT INSTRUCTOR, COURSE FROM Courses")
    for row in cursor.fetchall():
        print(row)

    print("3) Sadece 21 yaşındaki öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE AGE = 21")
    for row in cursor.fetchall():
        print(row)

    print("4) Sadece Chicago'da yaşayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE CITY = 'Chicago'")
    for row in cursor.fetchall():
        print(row)

    print("5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE INSTRUCTOR = 'Dr. Anderson'")
    for row in cursor.fetchall():
        print(row)

    print("6) Sadece ismi 'A' ile başlayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE NAME  LIKE 'A%'")
    for row in cursor.fetchall():
        print(row)

    print("7) Sadece 3 ve üzeri kredi olan dersleri getirin")
    cursor.execute("SELECT * FROM Courses WHERE CREDIT >= 3")
    for row in cursor.fetchall():
        print(row)

    # DETAILED
    print("\nDETAILED QUESTIONS")
    print("1) Öğrencileri ters alfabetik şekilde dizerek getirin")
    cursor.execute("SELECT * FROM Students ORDER BY NAME DESC")
    for row in cursor.fetchall():
        print(row)

    print("2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin")
    cursor.execute("SELECT * FROM Students WHERE AGE > 20 ORDER BY NAME")
    for row in cursor.fetchall():
        print(row)

    print("3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE CITY IN ('New York', 'Chicago')")
    for row in cursor.fetchall():
        print(row)

    print("4) Sadece 'New York' ta yaşamayan öğrencileri getirin")
    cursor.execute("SELECT * FROM Students WHERE CITY <> 'New York'")
    for row in cursor.fetchall():
        print(row)

def main():
    conn, cursor = connect_database()

    try:
        create_tables(cursor)
        insert_data(cursor)
        conn.commit()
        # basic_sql_operations(cursor)
        # sql_insert_update_delete_operations(conn, cursor)
        # aggregate_functions(cursor)
        questions_and_answers(cursor)
    except sqlite3.Error as err:
        print(err)
    finally:
        conn.close()

if __name__ == "__main__":
    main()