# 유튜브에 아이유 검색 -> 동영상들 제목만 추출
from click import option
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.headless = True  # 브라우저 창을 띄우지 않음
b = webdriver.Chrome(options=options)
b.maximize_window()
b.get("https://www.youtube.com/")

time.sleep(3)

# 검색어 '아이유' 입력
search = b.find_element(By.NAME, "search_query")
search.send_keys("아이유")
search.send_keys(Keys.ENTER)
time.sleep(2)

# 검색결과 출력
titles = b.find_elements(By.TAG_NAME, "h3")
for title in titles:
    print(title.text)

time.sleep(3)
b.quit()
