# csv 파일 입출력 (csv : 콤마형태로 분리된 파일)
import csv

# with open("data/sample1.csv", "r") as f:
#     reader = csv.reader(f)
#     # 헤더명 제거
#     next(reader)

#     print(reader)
#     print(type(reader))
#     print(type(dir(reader)))
#     print()
#     for c in reader:
#         print(c)

# with open("data/sample2.csv", "r") as f:
#     reader = csv.reader(f, delimiter="|")  # |를 ,로 바꿔줌...
#     for c in reader:
#         print(c)

# csv ==> dict 형태로 읽어오기
# with open("data/sample1.csv", "r") as f:
#     reader = csv.DictReader(f)

#     for c in reader:
#         print(c)  # 딕셔너리 형태로 출력됨
#         for k, v in c.items():
#             print(k, v)
#         print()

# with open("data/sample3.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)

#     for c in reader:
#         print(c)


# 1차원 리스트를 csv 파일로 저장
# list1 = [1, 2, 3, 4, 5]  # list1 = list(range(1,6))

# with open("data/sample4.csv", "w") as f:
#     write = csv.writer(f)

#     write.writerow(list1)  # writerow : 줄단위로 적겠다

list1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
]

# 줄마다 엔터가 한번씩 들어가있다.
# 엔터가 안들어가게 해주고 싶으면 newline=""
with open("data/sample5.csv", "w", newline="") as f:

    write = csv.writer(f)

    # for row in list1:
    #     write.writerow(row)

    # write.writerows(list1) # 확인없이 한번에 넣을 때 사용
