import pyautogui

# 마우스 액션 - click, doubleclick, drag and drop, scroll

# 클릭 - 왼/오 클릭
# click() : 현재위치에서 왼쪽 클릭
# click(x,y) : x,y좌표에서 왼쪽 클릭

# pyautogui.sleep(3)
# print(pyautogui.position())

# pyautogui.click(888, 27, duration=0.5)

# click(clicks=n) : n=2인 경우 더블클릭
pyautogui.sleep(3)
# pyautogui.click(clicks=5)

# 2초간격으로 오른쪽 버튼 2번 클릭
# pyautogui.click(clicks=2, interval=2, button="right")

# pyautogui.doubleClick(700, 7)

# pyautogui.rightClick(500,300)

# mouseDown() / mouserUp()
# pyautogui.moveTo(200,200)
# pyautogui.mouseDown(300,300)
# pyautogui.mouseUp()

# drag(x,y) 상대 / dragTo(x,y) 절대
# pyautogui.position()
# print(pyautogui.position()) 664,132

# 메모장이 있는 곳으로 이동
# pyautogui.moveTo(664, 132)
# pyautogui.drag(300, 0, duration=0.5)
# pyautogui.dragTo(200, 200, duration=0.5)


# scroll (값) : 값이 음수면 아래로, 양수면 위로
# pyautogui.scroll(400)
