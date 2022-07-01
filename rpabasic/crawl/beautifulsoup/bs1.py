# requests + beautifulsoup4(https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
# 객체생성(페이지소스, 파서(lxml))
# parsing : 원하는 데이터 가져오기

import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.v.daum.net/v/20220701153900549")
# print(res.text)

# parser : html.parser(default : 설치필요x), lxml(빠름, c언어기반)
# soup = BeautifulSoup(res.text, "html.parser")
soup = BeautifulSoup(res.text, "lxml")
# print(soup)  # 일반출력
# print(soup.prettify())  # 이쁘게(들여쓰기)

# <head> 태그 가져오기
# print(soup.head)

# <body> 태그 가져오기
# print(soup.body)

# <title> 태그 가져오기
# print(soup.title)  # 태그전체
# print(soup.title.name)  # 태그명
# print(soup.title.get_text())  # 태그 안 텍스트
# print(soup.title.string)  # 태그 안 텍스트


# 기사 제목 가져오기
title = soup.find("h3")
print(title.get_text())

# 기사 작성날짜와 시간 가져오기
date = soup.find("span", class_="num_date")
print(f"작성날짜 및 시간 : {date.get_text()}")

# 기사 작성자 가져오기
writer = soup.find("span", "txt_info")
print(f"작성자 : {writer.get_text()}")

# 기사 첫번째 문장 가져오기
paral = soup.find("p")
print(paral.get_text())
print()

# 기사 첫번째 문단 가져오기
contents = soup.find_all("p")
# print(contents)
for paral in contents:
    print(paral.get_text())
