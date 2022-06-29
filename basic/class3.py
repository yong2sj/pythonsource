# 클래스 변수
class UserInfo:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

        # 클래스 변수 : 자바에서 static 과 같은 개념
        UserInfo.user_cnt += 1

    def user_info(self):
        return "name : {}, age: {}".format(self.name, self.age)

    def __del__(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("홍길동", 25)
user2 = UserInfo("성춘향", 26)

print(user1.user_info())
print(user2.user_info())

print("현재 생성된 User {}명".format(UserInfo.user_cnt))

# 객체 삭제
del user1  # __del__ 호출
print("현재 생성된 User {}명".format(UserInfo.user_cnt))
