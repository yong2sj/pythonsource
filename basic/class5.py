# 클래스 메소드
class Test:
    # 인자로 self가 없는 경우 class 메소드
    def function1():
        print("function1 호출")

    def function2(self):
        print("function2 호출")


obj1 = Test()
# obj1.function1()  # TypeError: Test.function1() takes 0 positional arguments but 1 was given
Test.function1()
obj1.function2()

# TypeError: Test.function1() takes 0 positional arguments but 1 was given
# function1 에 self가 없어서 생긴 에러


# 생성자 오버로딩은 없음
class UserInfo:
    """
    UserInfo class
    Author : 홍길동
    Date : 2022-05-26
    Description : 클래스 작성법
    """

    user_cnt = 0

    def __init__(self, name, age, email=None) -> None:
        # email 값이 들어오면 들어온값으로 하고 안들어오면 None
        self.name = name
        self.age = age
        self.email = email
        # 클래스 변수 : 자바에서 static 과 같은 개념
        UserInfo.user_cnt += 1

    def user_info(self):
        return "name : {}, age: {}, email: {}".format(self.name, self.age, self.email)

    def __del__(self):
        UserInfo.user_cnt -= 1


user1 = UserInfo("홍길동", 30)
print(user1.user_info())

user2 = UserInfo("성춘향", 30, "sung@naver.com")
print(user2.user_info())
