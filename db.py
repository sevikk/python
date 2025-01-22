import sqlite3

DB_NAME = "sqlite_db.db"

# with sqlite3.connect(DB_NAME) as sqlite:
#     print(sqlite)
#     print(sqlite3.version)

# Create new table
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (
#     id integer PRIMARY KEY,
#     title text NOT NULL,
#     students_qty integer,
#     reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)


# Add record to courses table
# courses = [
#     (4, '1 course', 100, 20),
#     (5, '2 course', 100, 90),
#     (6, '3 course', 100, 155)
# ]

# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?,?,?,?)"
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)
        
#     sqlite_conn.commit()


with sqlite3.connect(DB_NAME) as sqlite_conn:
    sql_request = "SELECT * FROM courses WHERE reviews_qty<40"
    sql_cursor = sqlite_conn.execute(sql_request)
    # for record in sql_cursor:
    #     print(record)

    records = sql_cursor.fetchall()
    print(records)




