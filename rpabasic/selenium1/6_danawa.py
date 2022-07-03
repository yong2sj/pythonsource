from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 다나와 접속
b = webdriver.Chrome()
b.maximize_window()
b.get("https://www.danawa.com")
time.sleep(1)

# 로그인 버튼 찾기
login = b.find_element(By.CLASS_NAME, "btn_user--login")
login.click()
time.sleep(1)

# 아이디 입력칸 찾기
userid = b.find_element(By.ID, "danawa-member-login-input-id")
userid.clear()
userid.send_keys("아이디")

# 비밀번호 입력칸 찾기
userpw = b.find_element(By.ID, "danawa-member-login-input-pwd")
userpw.clear()
userpw.send_keys("비밀번호")
userpw.send_keys(Keys.ENTER)

time.sleep(3)
b.quit()
