# 한국은행 경제 통계시스템 엑셀 다운로드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 한국은행 경제 통계시스템 페이지 접속
b = webdriver.Chrome()
b.maximize_window()
b.get("http://ecos.bok.or.kr")
time.sleep(3)

# 1. 100대 지표 클릭
# selector : #root > div.wrap-body > div > div.main-wrap.clearfix > div.main-row3.clearfix > div.main-left > div.main-icon-menu > ul > li:nth-child(1) > a
# XPath : //*[@id="root"]/div[5]/div/div[2]/div[4]/div[1]/div[3]/ul/li[1]/a
b.find_element(
    By.XPATH, '//*[@id="root"]/div[5]/div/div[2]/div[4]/div[1]/div[3]/ul/li[1]/a'
).click()
time.sleep(2)

# 2. 엑셀 다운로드 버튼 찾기
# selector : #root > div.wrap-body > div > div.statics_header > div > div.searchBox > div.exelDown.partition-right > button
b.find_element(
    By.CSS_SELECTOR,
    "#root > div.wrap-body > div > div.statics_header > div > div.searchBox > div.exelDown.partition-right > button",
).click()

time.sleep(3)
b.quit()
