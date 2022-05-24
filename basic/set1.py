# set : 집합
# 자바 Set 과 같은 개념
# 중복 허용x
# 순서x - 인덱싱, 슬라이싱 하용할 수 없음 (순서가 없기떄문에)


set1 = set()
set2 = set("Hello")
set3 = set([1, 2, 3, 4])
set4 = set([1, 2, 3, 4, 6, 6])
set5 = set({"no": "1", "name": "hong", "age": 24})

print(set1)
print(set2)
print(set3)
print(set4)
print(set5)

print()

# set -> tuple 변환
print(tuple(set3))

# set -> list 변환
print(list(set3))
print()

# 교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print("s1,s2 교집합", s1 & s2)
print("s1,s2 교집합", s1.intersection(s2))

print()

print("s1,s2 합집합", s1 | s2)
print("s1,s2 합집합", s1.union(s2))

print()

print("s1,s2 차집합", s1 - s2)
print("s1,s2 차집합", s1.difference(s2))

print()

# 함수
# add() : 값 하나 추가
print(s1)
s1.add(17)
print(s1)
print()

# update() : 여러 개의 값을 한꺼번에 추가
s1.update([18, 19, 20])
print(s1)
print()

# remove() : 특정 값 제거
s1.remove(2)
print(s1)

# 숫자
# 문자열 : 인덱싱, 슬라이싱
# 리스트 : 인덱싱, 슬라이싱, 중요
# 튜플 : 인뎅싱, 슬라이싱, 값 변경 불가
# 딕셔너리 : key값을 value 가져오기(key중복불가)
# 집합 : 인덱싱, 슬라이싱 사용불가
