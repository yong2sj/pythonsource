# 파일 읽고 쓰기

# open("파일명",모드,encoding...) : 파일을 읽거나 쓸 때 사용

# f = open("data/test1.txt", "w", encoding="utf-8")  # write모드가 파일이 없다하더라도 실행됨
# print(dir(f))
# f.write("안녕하세요 \n반갑습니다.")  # 한글 깨지므로 encoding 필요
# f.close()  # 작업완료 후 close 로 닫아주자

# close 안쓰고 할 수 있음.
# with open("data/test1.txt", "w", encoding="utf-8") as f:
#     f.write("안녕하세요.\n반갑습니다.")

# 1~10 까지 파일로 작성
# f = open("data/test1.txt", "w", encoding="utf-8")
# w : 기존에 있던 파일에 덮어쓰기
# a : 기존에 있던 파일에 이어쓰기
# for i in range(1, 11):
#    f.write("%d\n" % i)
# f.close()

# with open("data/test1.txt", "w", encoding="utf-8") as f:
#    for i in range(1, 11):
#        f.write("%d\n" % i)

# list 를 파일로 작성
# list = ["홍길동", "김길동", "이길동"]
# list = ["홍길동\n", "김길동\n", "이길동\n"]
# f = open("data/test1.txt", "w", encoding="utf-8")
# f.write(list)  # TypeError: write() argument must be str, not list
# f.writelines(list)  # list를 작성하려면 f.writelines
# f.close()


# list 를 파일에 쓰려면 for문 + write()
#                       writelines()
# list = ["홍길동", "김길동", "이길동"]
# f = open("data/test1.txt", "w", encoding="utf-8")

# for i in list:
#    f.write(i + "\n")
# f.close()


# 딕셔너리 구조 파일로 작성
# dict1 = {"name": "hong", "age": 25, "addr": "서울"}
# f = open("data/test1.txt", "w", encoding="utf-8")
# f.writelines(dict1) # nameageaddr : key값만 넣어진다
# for k, v in dict1.items():
#    f.writelines("{} : {}\n".format(k, v))
# f.close()


# 1000 명의 키와 몸무게를 랜덤으로 생성한 후 파일 작성
# import random

# list1 = list("가나다라마바사아자차카타파하")
# print(list1)

# f = open("data/info.txt", "w", encoding="utf-8")

# choice(list1) : 무작위로 하나
# randragne(40, 100) : 40 ~ 100 사이 임의의 숫자
# for i in range(1000):
#    name = random.choice(list1) + random.choice(list1)
#    weight = random.randrange(40, 100)
#    height = random.randrange(140, 200)
#    f.writelines("{}, {}, {}\n".format(name, weight, height))

# f.close()
