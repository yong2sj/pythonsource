import sqlite3

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# 수정
# id가 2번인 user이름을 cho로 변경

# sql = """update users set username = ? where id = ?"""

# cursor.execute(sql, ("cho", 2))  # sql 옆에는 ?에 해당하는 값 넣기
# conn.commit()


# 딕셔너리 구조
# sql = """update users set username = :username where id = :id"""

# cursor.execute(sql, {"username": "hong", "id": 2})
# conn.commit()


# %s
sql = """update users set username = '%s' where id = '%s'"""

cursor.execute(sql % ("cho", 2))
conn.commit()


# 삭제
cursor.execute("delete from users where id = ?", (2,))
cursor.execute("delete from users where id=:id", {"id": 3})
cursor.execute("delete from users where id=%d" % 4)

conn.commit()
