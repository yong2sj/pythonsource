# 사업자등록상태 조회 자동화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from bs4 import BeautifulSoup

b = webdriver.Chrome()
b.get(
    "https://teht.hometax.go.kr/websquare/websquare.html?w2xPath=/ui/ab/a/a/UTEABAAA13.xml"
)
b.maximize_window()

# 사업자등록번호 입력
# 767-82-00017
b.find_element(By.ID, "bsno").send_keys("767-82-00017")

# 조회하기 클릭
b.find_element(By.ID, "trigger5").click()

time.sleep(1)

# 상태 화면 출력
# tbody = b.find_element(By.XPATH, '//*[@id="grid2_body_tbody"]')
# print(tbody.text) # 767-82-00017 부가가치세 일반과세자 입니다. 2022-06-23

soup = BeautifulSoup(b.page_source, "lxml")

tds = soup.select("#grid2_body_tbody > tr > td")

for td in tds:
    print(td.get_text())


time.sleep(3)
b.quit()
