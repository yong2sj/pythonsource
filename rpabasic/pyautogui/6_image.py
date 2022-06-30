# 이미지 인식
import pyautogui as p

# confidence : 신뢰도 (default 1, 0.8 ~ 0.9로 설정)
# -> opoencv-python 라이브러리 설치해야함
# -> pip install opencv-python
# locateOnScreen(path, confidence) : 캡처한 이미지의 화면상 좌표 구하기
# 이미지 기반이어서 해상도가 바뀐다거나 이런 경우는 잘 안됨

# screen_locate = p.locateOnScreen("./rpabasic/pyautogui/screen1.png", confidence=0.9)
# print(screen_locate)  # Box(left=0, top=0, width=300, height=400)

# screen_locate = p.locateOnScreen("./rpabasic/pyautogui/file_menu.png")
# print(screen_locate)  # Box(left=803, top=4, width=63, height=40)

# locateAllOnScreen() : 찾아야 하는 이미지가 여러개 있는 경우
# p.sleep(2)
# for i in p.locateAllOnScreen("./rpabasic/pyautogui/checkbox.png", confidence=0.9):
#     print(i)
#     p.click(i)

# 찾아야 하는 대상이 화면에 늦게 나타나는 경우

# 찾을 때까지 반복시키기
# checkbox = p.locateOnScreen("./rpabasic/pyautogui/checkbox.png", confidence=0.9)
# while checkbox is None:
#     checkbox = p.locateOnScreen("./rpabasic/pyautogui/checkbox.png", confidence=0.9)
#     print("발견할 수 없음")

# p.click(checkbox)

# 일정시간만 기다리기
import time, sys

timeout = 5
start = time.time()
checkbox = p.locateOnScreen("./rpabasic/pyautogui/checkbox.png", confidence=0.9)
while checkbox is None:
    checkbox = p.locateOnScreen("./rpabasic/pyautogui/checkbox.png", confidence=0.9)

    end = time.time()

    if end - start > timeout:
        print("시간초과")
        sys.exit()

p.click(checkbox)
