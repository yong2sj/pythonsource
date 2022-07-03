from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Chrome()
b.maximize_window()
b.get("http://www.naver.com")

# 두번째 탭을 연 후에 daum 접속
# 스크립트 새창 열기
b.execute_script("window.open('http://www.daum.net')")
time.sleep(1)
print("title : {}".format(b.title))  # NAVER

# 현재 브라우저에 열린 탭 가져오기
tabs = b.window_handles  # tabs[0] : 처음 접속 페이지

b.switch_to.window(tabs[1])
print("2. title : {}".format(b.title))

element = b.find_element(By.NAME, "q")
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(1)

# 네이버로 돌아가기
b.switch_to.window(tabs[0])


time.sleep(3)
b.quit()
