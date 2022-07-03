# gmarket 접속하고 상품명 입력한 후 결과 페이지 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# gmarket 접속
b = webdriver.Chrome()
b.maximize_window()
b.get("https://www.gmarket.co.kr/")
time.sleep(1)

# 검색창 찾기
search = b.find_element(By.NAME, "keyword")

# 검색어 입력
search.send_keys("마스크")
search.send_keys(Keys.ENTER)


time.sleep(3)
b.quit()
