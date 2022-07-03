from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# iframe : 하나의 html안에 html 태그를 또 씀
b = webdriver.Chrome()
b.maximize_window()
b.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_headers")
time.sleep(1)

# iframe 안의 태그 찾기
# iframe 안으로 들어가서 찾아야함
b.switch_to.frame("iframeResult")

ele = b.find_element(By.TAG_NAME, "h1")  # NoSuchElementException
print(ele.text)

# iframe 밖으로 나오기
b.switch_to.default_content()
left = b.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[12]/span/span[10]',
)
print(left.text)

time.sleep(3)
b.quit()
