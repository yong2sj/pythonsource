# 함수
# 반복적으로 수행되는 부분을 함수로 작성
# 단독 실행 가능

# def 함수명():
#   수행할 문장1
#   수행할 문장2


# def hello():
#    print("hello!!!")


# def add(a, b):
#    return a + b

# result = add(3, 4)
# print(result)

# return
def sum_and_mul(a, b):
    return a + b, a * b  # tuple을 사용해서 리턴됨


print(sum_and_mul(4, 5))  # (9,20)
print()

add, mul = sum_and_mul(7, 6)
print(add, "", mul)
print()


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return y1, y2, y3


print(func_mul(100))

y1, y2, y3 = func_mul(200)
print("%d, %d, %d" % (y1, y2, y3))


# 기본 파라메터
def print_n_times(value, n=2):
    for i in range(n):
        print(value)


# print_n_times("안녕하세요")  # n이 안넘어왔으므로 위처럼 기본값 2로 실행
# print()
# print_n_times("안녕하세요", 5)  # n값 5로 지정


# def say_myself(name, old, man=True):
#    print("나의 이름은 %s 입니다" % name)
#    print("나의 나이는 %d 입니다" % old)

#    if man:
#        print("남자입니다.")
#    else:
#        print("여자입니다.")


# say_myself("홍길동", 27)  # 성별 미입력시. 위에 기본값은 man으로 나옴
# say_myself("홍길동", 27, False)
# say_myself("홍길동", 32, True)

# *args : 가변 파라메터(인자의 개수가 정확하지 않을 때)
# args 는 변경 가능함


def add_many(*args):
    print(type(args))  # tuple
    print(args)


add_many({"desert": "macaroon", "wine": "merlot"})
add_many("35", "24", "15", "36")
add_many([35, 24, 18, 17])
add_many(1, 2, 3, 4, 5, 6)
add_many()


def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print("result =", add_many())
print("result =", add_many(15, 63, 45, 356, 36, 9, 3))
print("result =", add_many(27, 35, 56))
print("result =", add_many(39, 48, 17, 16, 15))
print()

# **kwargs : 가변 파라메터를 딕셔너리 형태로 처리
# def args_func1(**kwargs):
#    print("kwargs", kwargs)
#
#    for k in kwargs.keys():
#        print(k)

#   for k, v in kwargs.items():
#       print(k, v)
#   print()


# args_func1(name="kim")
# args_func1(name="kim", name2="park", active="Test")
# args_func1(name="kim", age=10, title="Title")
# args_func1(name="kim", age=25, addr="서울")


# def example_mul(arg1, arg2=5, *args, **kwargs):
#    print(arg1, arg2, args, kwargs)


# example_mul(10, 20)
# example_mul(10)
# example_mul(10, 20, "park", "Kim", 10, 20)
# example_mul(10, 20, "choi", age=25, name="Kim")

# 함수 안에서 선언된 변수의 효력 범위
# func을 벗어나면 의미가 없다
a = 1


# def var_test(a):
#    a = a + 1
#    return a


# a = var_test(a)
# var_test(a)
# print(a)


def var_test():
    global a  # global 함수 밖에 있는 변수를 불러다가 쓰겠음.
    a = a + 1


var_test()
print(a)


# 실습
# 2개의 인자와 연산자를 받아서 사칙 연산을 수행하는 함수(four_rules) 작성
# 인자와 연산자는 사용자에게 입력받는 형태로 작성


# def test(a, b):
#   print(a, "+", b, "=", a + b)
#    print(a, "-", b, "=", a - b)
#    print(a, "*", b, "=", a * b)
#    print(a, "/", b, "=", a / b)


# a = int(input("input a : "))
# b = int(input("input b : "))
# test(a, b)


# def four_rules(num1, num2, op):
#   if op == "+":
#       return num1 + num2
#   elif op == "-":
#        return num1 - num2
#   elif op == "*":
#       return num1 * num2
#    else:
#        return num1 / num2


# num1 = int(input("Num1 : "))
# num2 = int(input("Num2 : "))
# op = input("+,-,*,/ 중 하나의 연산자 : ")
# print("%d %c %d = %d" % (num1, op, num2, four_rules(num1, num2, op)))


# [[1,2,3],[4,5,6],[7,8,9]] 형태의 리스트를 받아 1차원 리스트로 반환


# def flatten(data):
#   output = []
#
#   for item in data:
#      if type(item) == list:
#         output += flatten(item)
#    else:
#       output.append(item)
# return output
#
#
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(flatten(list1))

# 로또 생성기
import random


def get_number():
    return random.randrange(1, 46)


# lotto 리스트에 6개의 숫자가 다 채워질때까지 get_number()를 호출하는 코드 작성

lotto = []

while True:
    num = get_number()

    if lotto.count(num) == 0:
        lotto.append(num)

    if len(lotto) >= 6:
        break

lotto.sort()
print("이번 주 로또 번호 ", lotto)
