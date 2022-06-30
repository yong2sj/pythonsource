import pyautogui

# 좌표인식 : position()

pos = pyautogui.position()
print(pos)  # Point(x=1835, y=73)
print(pos.x, ", ", pos.y)  # x축,y축 따로 출력

# 마우스 이동 - moveTo() / moveRel()
# moveTo : 절대좌표 / moveRel : 상대좌표
# pyautogui.moveTo(x=100, y=100, duration=1)

pyautogui.moveTo(300, 300, duration=1)
pyautogui.moveRel(100, 199, duration=0.5)
print(pyautogui.position())
