from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Chrome()
b.maximize_window()
b.get("https://shopping.naver.com/home/p/index.naver")

# 검색창 찾기
search = b.find_element(By.CLASS_NAME, "_searchInput_search_input_QXUFf")
search.send_keys("마우스")
# search.send_keys(Keys.ENTER)

# 버튼 클릭
b.find_element(By.CLASS_NAME, "_searchInput_button_search_1n1aw").click()

# 스크롤 이동 : window.scrollTo(x,y)
# b.execute_script("window.scrollTo(0,1080)")
# b.execute_script("window.scrollTo(0,2160)")

# 끝으로 스크롤
b.execute_script("window.scrollTo(0,document.body.scrollHeight)")
# 동적페이지 스크롤링
# 3초에 한번씩 스크롤 이동
interval = 3

# 현재 문서 높이 가져와서 저장
prev_height = b.execute_script("window.scrollTo(0,document.body.scrollHeight)")

while True:
    # 스크롤 이동
    b.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 스크롤이 진행된 후 현재 문서 높이
    curr_height = b.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    if curr_height == prev_height:
        break
    prev_height = curr_height

# 맨 처음으로 이동
b.execute_script("window.scrollTo(0,0)")

time.sleep(3)
b.quit()
