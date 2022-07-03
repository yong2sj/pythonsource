# pip install selenium
# 셀레니움 - 브라우저 자동화 개념 적용
#            webdriver 이용해서 브라우저 조작해서 자동으로 일을 시킬 수 있음
#            웹을 테스트하기 위한 프레임워크
#            자바, 파이썬, C#, 자바스크립트 등 언어들에서 사용가능
#            소스가져오기 + 파싱도 가능
#            브라우저로 접근하기 때문에 차단될 확률도 적어짐

from selenium import webdriver
import time

# . : pythonsource 에 chromedriver 위치
browser = webdriver.Chrome()

# 특정 사이트 연결
browser.get("https://www.naver.com")

time.sleep(3)
# 브라우저 닫기
browser.quit()
