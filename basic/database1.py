# db연동
# SQLite : 내장 DB / python / spring boot
# https://sqlitebrowser.org/dl/
# DB Browser for SQLite - Standard installer for 64-bit Windows 설치

import sqlite3
from datetime import datetime

print(sqlite3.version)
print(sqlite3.sqlite_version)

# 날짜 생성
now = datetime.now()
# print("now", now)
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print("now_date_time", now_date_time)

conn = sqlite3.connect("data/database.db", isolation_level=None)

# 커서
cursor = conn.cursor()
print(type(cursor))  # <class 'sqlite3.Cursor'>

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, phone text, website text, regdate text)"
)

# INSERT
# cursor.execute(
#     "INSERT into users VALUES(1,'KIM','010-1234-5678','kim.com',?)",
#     (now_date_time,),  # 튜플의 형태로 넣어야함
# )

# INSERT2
# cursor.execute(
#     "INSERT into users VALUES(?,?,?,?,?)",
#     (2, "hong", "010-5678-1234", "hong.com", now_date_time),
# )

# INSERT3 (여러개 삽입)
user_list = (
    (3, "park", "010-5678-5678", "park.com", now_date_time),
    (4, "choi", "010-1234-1234", "choi.com", now_date_time),
    (5, "yoo", "010-1234-4321", "yoo.com", now_date_time),
)

cursor.executemany("INSERT INTO users VALUES(?,?,?,?,?)", user_list)
