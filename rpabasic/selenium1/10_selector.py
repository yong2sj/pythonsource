from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

b = webdriver.Chrome()
b.get("http://python.org")
b.maximize_window()

# 결과 페이지에서 원하는 요소 찾기 - 기준 부여
# find_element() : 하나의 요소 / find_elements() : 여러개 요소(list)

# 기준 - By
# By.NAME
# By.CLASS_NAME
e = b.find_element(By.CLASS_NAME, "search-field")
# By.CSS_SELECTOR
e = b.find_element(By.CSS_SELECTOR, "#id-search-field")
# By.ID
e = b.find_element(By.ID, "id-search-field")
# By.LINK_TEXT
# By.TAG_NAME
# By.PARTIAL_LINK_TEXT
# By.XPATH
e = b.find_element(By.XPATH, '//*[@id="id-search-field"]')

e.send_keys("python")
e.send_keys(Keys.ENTER)

time.sleep(3)
b.quit()
