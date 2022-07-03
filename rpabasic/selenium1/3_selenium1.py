from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()  # 창 최대화

print(browser.current_url)  # https://www.daum.net/
print(browser.title)  # Daum

# 테스트 코드
# browser.title 에 Daum 문구가 없으면 error 발생
# 이 후 코드는 실행 안함
assert "Daum" in browser.title

# 현재 페이지 소스 가져오기
print(browser.page_source)

# 세션id 가져오기
print(browser.session_id)

# 쿠키 정보 가져오기
print(browser.get_cookies)

time.sleep(3)
browser.quit()
