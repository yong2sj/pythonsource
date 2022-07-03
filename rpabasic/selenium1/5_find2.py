from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

b = webdriver.Chrome()
b.get("http://python.org")
b.maximize_window()

# 검색 창 찾기
ele = b.find_element(By.ID, "id-search-field")

# 검색 창 초기화
ele.clear()

# 검색어 입력
ele.send_keys("python")
ele.send_keys(Keys.ENTER)
time.sleep(1)

# 결과페이지에서 원하는 요소 추출
# ** selenium / beautifulsoup 둘 중 하나 이용.

# selenium 방식
# titles = b.find_elements(By.TAG_NAME, "h3")

# for title in titles:
#     print(title.text)

# BeautifulSoup 방식
res = BeautifulSoup(b.page_source, "lxml")
titles = res.find_all("h3")

for title in titles:
    print(title.get_text())


time.sleep(3)
b.quit()
