# 주차장 프로그램 작성
# 1. 다음과 같은 메뉴를 제공한다
#   1) 자동차 넣기     2) 자동차 빼기     3) 종료
# 2. 사용자는 메뉴에서 1~3번 사이의 메뉴만 선택할 수 있도록 한다.
# 3. 1번을 선택한 경우 다음과 같은 출력이 나오도록 한다.
#   ex) A자동차 들어감. 주차장 상태 ==> ['A']
# 4. 2번을 선택한 경우 다음과 같은 출력이 나오도록 한다.
#   ex) E자동차 나감. 주차장 상태 ==> ['A', 'B', ]
# 5. 3번을 선택한 경우 프로그램을 종료하도록 한다.

parking = []

top, car_name = 0, "A"

# ord("A") => 65
# print(ord(car_name))
# print(ord(car_name) + 1)
# print(chr(ord(car_name) + 1))

while True:
    no = int(input("[1] 자동차 넣기 | [2] 자동차 빼기 | [3] 종료 : "))

    if no <= 3:
        if no == 1:
            if top >= 5:
                print("만차입니다.")
            else:
                parking.append(car_name)
                print("%s 자동차 들어감. 주차장 상태 ==> %s" % (car_name, parking))
                top += 1
                car_name = chr(ord(car_name) + 1)

        elif no == 2:
            if top > 0:
                out_car = parking.pop()
                print("%s 자동차 나감. 주차장 상태 ==? %s" % (out_car, parking))

                top -= 1
                car_name = chr(ord(car_name) - 1)
            else:
                print("빠져나갈 자동차 없음")

        else:
            print("프로그램 종료")
            break

    else:
        print("번호를 확인해주세요")
