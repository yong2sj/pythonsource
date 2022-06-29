# json 읽고 쓰기
import json

data = (
    '{"id": "hong", "language": "python","edition": "3.9","author": "Guido van Rossum"}'
)

# 문자열 형태를 json 로드
# json_data = json.loads(data)

# print(
#     type(json_data),
#     json_data["id"],
#     json_data["language"],
#     json_data["edition"],
#     json_data["author"],
# )

# data = {
#     "id": "hong",
#     "language": "python",
#     "edition": "3.9",
#     "author": "Guido van Rossum",
# }

# # 딕셔너리 형태를 불러올 때 사용
# json_data = json.dumps(data)

# print(type(json_data))
# print(json_data)

# data = {
#     "id": "hong",
#     "language": "python",
#     "edition": "3.9",
#     "author": "Guido van Rossum",
# }

# key, value 추가
# data["language"] = ["java", "script"]

# with open("data/test1.json", "w") as f:
#     json.dump(data, f, indent=2)  # indent=2 : 들여쓰기 하겠다

# with open("data/test1.json", "r") as f:
#     json_data = json.load(f)

#     print(json_data)

with open("data/user.json", "r") as f:
    json_data = json.load(f)

    # print(json_data)
    for person in json_data:
        # print(person)  # 한사람씩 볼 수 있다.
        for k, v in person.items():
            print(k, v)
