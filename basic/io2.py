# 파일 읽기

# with open("data/review.txt", "r", encoding="utf-8") as f:
#    print(f.read())

# with open("data/review.txt", "r", encoding="utf-8") as f:
# print(f.readline()) # 줄단위로 읽어옴
#    line = f.readline()
#    while line:
#        print(line, end="")
#        line = f.readline()


# 파일의 내용을 리스트로 가져오기
# with open("data/review.txt","r",encoding="utf-8") as f:
#    print(f.readlines())


# score.txt 읽어서 평균 출력하기
# score = []
# with open("data/score.txt", "r", encoding="utf-8") as f:
# print(f.readlines())
#    for num in f:
#        score.append(int(num))
#    print(score)

# print("평균 : %.2f" % (sum(score) / len(score)))

# 총합과 평균을 result.txt 파일로 작성
# 총합 :
# 평균 :

# with open("data/score.txt", "r", encoding="utf-8") as f:
#     for num in f:
#         score.append(int(num))

# with open("data/result.txt", "w", encoding="utf-8") as f:
#     f.write("총합 : %d\n" % (sum(score)))
#     f.write("평균 : %.2f" % (sum(score) / len(score)))

# info.txt 읽은 후 BMI 지수를 계산한 후 화면 출력
# 나바, 96, 140
# 이름 : 나바
# 몸무게 : 96
# 키 : 140
# BMI : 계산값 (BMI = weight / (height/100) ** 2)
# 결과 : 과체중 (BMI 지수 25이상 과체중, 18.5이상 정상, 나머지 저체중)

# with open("data/info.txt", "r", encoding="utf-8") as f:
#     for info in f:
#         name, weight, height = info.strip().split(", ")
#         # strip : 공백제거, split 자르기
#         # print(name, weight, height)

#         bmi = int(weight) / (int(height) / 100) ** 2

#         result = ""
#         if 25 <= bmi:
#             result = "과체중"
#         elif 18.5 <= bmi:
#             result = "정상체중"
#         else:
#             result = "저체중"

#         print(
#             "\n".join(["이름 : {}", "몸무게 : {}", "키 : {}", "BMI : {}", "결과 : {}"]).format(
#                 name, weight, height, bmi, result
#             )
#         )

#         print()


# 원본 파일을 읽은 후 암호화, 암호화된 파일을 읽은 후 복호화 프로그램 작성

# content = ""

# while True:
#     no = int(input("1. 암호화 | 2.복호화 | 3. 종료 중 메뉴 입력 :"))

#     if no == 1:
# origin 읽은 후 content 라는 변수에 읽어온 내용 담기
# with open("data/origin.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)

# encryption.txt 작성
# 읽어온 내용 암호화 ord("c") :  99, (코드값 + 100 => 문자로 변경 : chr())
# ex) ord(안) -> 코드값 + 100 -> chr(안)
# chr(ord(c) + 100)
#     with open("data/encryption.txt", "w", encoding="utf-8") as f:
#         for c in content:
#             f.write(chr(ord(c) + 100))

# elif no == 2:
# encryption.txt 읽은 후 원래 있던 내용으로 출력
#     with open("data/encryption.txt", "r", encoding="utf-8") as f:
#         content = f.read()
#         for i in range(0, len(content)):
#             print(chr(ord(content[i]) - 100), end="" )
# else:
#     print("프로그램 종료")
#     break


# r,w, 이진 파일 - rb,wb
data = None
with open("c:\\windows\\notepad.exe", "rb") as f:
    data = f.read()

with open("c:\\temp\\notepad.exe", "wb") as f:
    f.write(data)
