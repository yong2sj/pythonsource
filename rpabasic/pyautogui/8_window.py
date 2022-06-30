import pyautogui as p

# getActiveWindow() : 현재 활성화된 창 가져오기
# w = p.getActiveWindow()
# print(w)
# print(w.title)
# print(w.size)
# print(w.left, w.right, w.top, w.bottom)
# p.click(w.left + 25, w.top + 20)

# getAllWindows() : 현재 윈도우에 떠있는 모든 창 가져오기
# for w in p.getAllWindows():
#     print(w)

# getWindowsWithTitle() : 특정 타이틀을 가진 창 모두 가져오기

w = p.getWindowsWithTitle("제목 없음")[0]
if not w.isActive:
    w.activate()

if not w.isMaximized:
    w.maximize()

p.sleep(1)

if not w.isMinimized:
    w.minimize()

p.sleep(1)
w.close()  # 프로그램 종료
