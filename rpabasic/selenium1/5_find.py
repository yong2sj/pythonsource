from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()

# 원하는 요소 찾기
# daum에서 아이폰을 검색해보자
# 1. 요소에서 검색창 찾기
element = browser.find_element(By.NAME, "q")
# print(element)
# <selenium.webdriver.remote.webelement.WebElement (session="8cbeb8489d4fbb540798e2f1615129de", element="7f0f94f7-635d-4403-9819-5b348b6c2706")>

# 2. 검색어 넣기
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

# 3. 검색결과 기다리기
time.sleep(1)

# 4. 뒤로가기
browser.back()

time.sleep(3)
browser.quit()
