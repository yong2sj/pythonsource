from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# iframe : 하나의 html안에 html 태그를 또 씀
b = webdriver.Chrome()
b.maximize_window()
b.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio")
time.sleep(1)

h1_element = b.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[5]/span/span[4]',
)
print(h1_element.text)

# iframe 안으로 이동
b.switch_to.frame("iframeResult")

# 첫번째 라디오 찾은 후 클릭
b.find_element(By.ID, "html").click()


time.sleep(3)
b.quit()
