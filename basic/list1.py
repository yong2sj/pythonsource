# list 자료형(배열과 같은 개념)
# 다양한 형태의 자료들을 담을 수 있음

# 생성
list1 = []
list2 = list(["a", "b", "c"])
list3 = ["a", "b", "c", 1, 2]
list4 = [1, 2, 3, 4, 5, 6.5]
list5 = [1, 2, ["Life", "is", "short"]]
list6 = list()

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print()

# 인덱싱
print("list2[0]", list2[0])
print("list3[-1]", list3[-1])
print("list4[3]", list4[3])
print("list4[3] + list5[1]", (list4[3] + list5[1]))
print("list5[2][0]", list5[2][0])
print("list5[-1][2]", list5[-1][2])
print()

# 슬라이싱
print("list2[0:3]", list2[0:3])
print("list3[-1]", list3[1:3])
print("list5[2:]", list5[2:])
print()

str = "Hello"

list7 = ["a", "b", [1, 2]]


list6 = [1, 2, ["a", "b", ["Life", "is"]]]

# is 출력
print("list6[2][2][1] = ", list6[2][2][1])
print("list6[-1][-1][-1] = ", list6[-1][-1][-1])
print("list6[2][-1][-1] = ", list6[2][-1][-1])
print()

# 연산자
# + : 연결, 인덱스 :
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = ["a", "b", "c"]

print("list1 + list2 = ", (list1 + list2))
print("list1 + list3 = ", (list1 + list3))
print("list1[0] + list2[1] = ", (list1[0] + list2[1]))
# print("list1[0] + list3[1] = ", (list1[0] + list3[1]))
print()

# *
print("a * 3 = ", (list1 * 3))
print("list1[0] * 3 = ", (list1[0] * 3))
print()

# 리스트 요소 값 변경
print("list1 = ", list1)
list1[1] = 7
print("list1 = ", list1)
list1[2] = "life"
print("list1=", list1)
print()

print("list2=", list2)
list2[1:2] = [10, 11]
print("list2=", list2)  # list2= [4, 10, 11, 6]
list2[1] = [15, 16, 17]
print("list2=", list2)  # list2= [4, [15, 16, 17], 11, 6]
# 범위 지정을 하면 그냥 밀어넣어지고, 범위지정없으면 리스트안에 리스트로 삽입됨
print()

# 리스트 요소 삭제
print("list1 = ", list1)
# del list1[2]
# del list1[1:3]
print("list1=", list1)
list1[1:3] = []
print("list1=", list1)

print()
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
for num in list1:
    print(num, end=" ")

print()

numbers = [273, 103, 5, 32, 65, 8, 72, 800, 99]
# 리스트 안의 숫자 중 100 이상인 숫자 출력
for num in numbers:
    if num >= 100:
        print("100이상인 숫자 = {}".format(num))
print()

# 리스트 안의 숫자가 홀수/짝수인지 판별
for num in numbers:
    if num % 2 == 0:
        print("{}는 짝수".format(num))
    else:
        print("{}는 홀수".format(num))

# 리스트 안의 숫자들의 자릿수 출력하기
# for num in numbers:
#    print("{}은 {}자리".format(num, len(str(num))))

print()

# 함수
# append() : 리스트에 요소 추가
list1 = [1, 2, 3]
list1.append(4)
list1.append([5, 6, 7])
print(list1)

print()
# 1~100까지의 숫자 중에서 짝수 리스트 생성
even = []
for i in range(1, 101):
    if i % 2 == 0:
        even.append(i)
print(even)
print()

# sort : 오름차순 정렬(기본), sort(reverse=True) : 내림차순
list1 = [1, 4, 3, 2]
print("정렬 전 ", list1)
list1.sort()
print("정렬 후 ", list1)
list1.sort(reverse=True)
print("내림차순 정렬", list1)

list2 = ["a", "x", "b", "y", "c", "z"]
list2.sort()
print("", list2)

list3 = ["A", "z", "C", "Y", "h", "L"]
list3.sort()
print("", list3)

list4 = ["ㄷ", "ㄱ", "ㄴ", "ㅁ", "ㅅ"]
list4.sort()
print("", list4)

#  reverse() : 리스트 뒤집기
list1 = ["a", "b", "c"]
list1.reverse()
print("", list1)
print()

# sort() + reverse()
list1 = [3, 12, 1, 5, 9, 2, 7]
list1.sort()
print("sort ", list1)

list1.sort(reverse=True)
print("sort.reverse ", list1)

list1.reverse()
print("reverse", list1)
print()

# index() : 위치 반환
print("list1", list1)
print("list1 에 9가 있는지 확인", list1.index(9))
# print("list1 에 45가 있는지 확인", list1.index(45))
# 45가 없어서 ValueError 발생
print()

# insert(삽입위치, 삽일할 요소)
list1 = [1, 2, 3]
list1.insert(0, 4)
print("list1 요소 삽입 후 ", list1)
print()

# remove(제거할 요소)
list1.remove(2)
print("list1 요소 제거 후 ", list1)

print()
# pop() : 리스트 요소 끄집어 내기
list1 = [1, 2, 2, 3, 4, 5, 6, 7]
print("list1", list1)
list1.pop()
print("pop사용", list1)
list1.pop(3)
print("pop사용", list1)
# list1.pop(1,3)
# print("pop 되나?", list1)
# 안되네....

print()
# count(x) : 리스트에 포함된 요소 x의 개수 세기
print("list1.count(2)", list1.count(2))

print()
# extend(x리스트) : 원래 리스트에 x 리스트 더하기
list2 = [15, 16, 17]
list1.extend(list2)
print("extend", list1)
list3 = [21, 22, 23]
print("list1+ list3 = ", (list1 + list3))
# list + 랑 같은 역할임

print()
# clear() : 모든 요소 삭제
list1.clear()
print("list1 clear()", list1)
print()

# 요소 in 리스트명
fruits = ["딸기", "사과", "수박", "바나나", "참외", "포도"]
print("딸기" in fruits)
print("두리안" in fruits)
print()


# 리스트에 비어있으면 거짓
list1 = []
if list1:
    print("참")
else:
    print("거짓")
print()

# 리스트 요소 출력
for num in numbers:
    print(num)
print()
for num in enumerate(numbers):
    print(num)  # (인덱스, 값) => 튜플 자료형
print()

# idx, num = (0,273)
for idx, num in enumerate(numbers, start=1):
    print(idx, num)
print()

# 실습
# A학급에 총 10명의 학생이 잇따. 이 학생들의 중간고사 점수는 다음과 같다
# 70,66,55,75,90,95,80,85,100,87
# 중간고사 점수를 리스트로 생성하고 A학급의 평균을 구하시오
A_class = [70, 66, 55, 75, 90, 95, 80, 85, 100, 87]
total = 0
for num in A_class:
    total += num
print("A학급의 평균 : %.2f" % (total / len(A_class)))
print("A학급의 평균 : %.2f" % (sum(A_class) / len(A_class)))
print()

# 다음 리스트에서 Apple 항목만 삭제하고 출력하기
# ["Banana","Apple","Orange","Grape"]

fruits = ["Banana", "Apple", "Orange", "Grape"]
fruits.remove("Apple")
print(fruits)
print()


