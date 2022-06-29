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
