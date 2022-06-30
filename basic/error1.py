# 예외 처리
# 문법 에러

print("test")

a, b = 10, 15
print(a, b)
# print(c)  # NameError: name 'c' is not defined

# print(10 / 0)  # ZeroDivisionError: division by zero

x = [10, 20, 30]
# print(x[3])  # IndexError: list index out of range

dict1 = {"name": "hont", "age": 25, "city": "seoul"}
# print(dict1["addr"])  # KeyError: 'addr'

# x.index(40)  # ValueError: 40 is not in list

# f = open("data/111.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory

x = [1, 2]
y = (1, 2)
# print(x + y)  # TypeError: can only concatenate list (not "tuple") to list

### 예외 처리 기법
# try ~ except 문 : 오류 종류와 상관없이 오류가 발생하기만 하면 except 블록 수행
# try ~ except 발생오류 : except에 정해놓은 오류 시 except 블록 수행
# try ~ except ~ else
# try ~ finally : 오류 발생 여부와 상관없이 무조건 실행(리소스 해제)


# name = ["Kim", "Park", "Choi"]

# try:
#     z = "let"
#     x = name.index(z)
#     print("{} Found it! in name {}".format(z, x + 1))
# except:
#     print("Not Found")

# try:
#     number = int(input("정수입력 >> "))

#     print("원 반지름 : ", number)
#     print("원 둘레 : ", 2 * 3.14 * number)
#     print("원 넓이 : ", 3.14 * number * number)
# except:
#     print("입력 숫자를 확인해주세요")

# try:
#     number = int(input("정수입력 >> "))

#     print("원 반지름 : ", number)
#     print("원 둘레 : ", 2 * 3.14 * number)
#     print("원 넓이 : ", 3.14 * number * number)
# except ValueError:  # ValueError 일 때만 수행
#     print("입력 숫자를 확인해주세요")

try:  # 예외 발생 구문
    pass
except:  # 예외가 발생한 경우
    pass
else:  # 예외가 발생하지 않은 경우에 실행 (except 절 바로 다음에 위치)
    pass

# try:
#     4 / 0
# except ZeroDivisionError as e:
#     print(e)

try:
    f = open("data/info.txt", "r")
finally:
    f.close()

try:  # 예외 발생 구문
    pass
except:  # 예외가 발생한 경우
    pass
else:  # 예외가 발생하지 않은 경우에 실행 (except 절 바로 다음에 위치)
    pass
finally:  # 예외 발생 여부 상관없이 무조건 실행
    pass
