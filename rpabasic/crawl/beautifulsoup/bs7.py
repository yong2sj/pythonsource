# css 선택자 이용한 요소 찾기 : select, select_one
# find select 는 개발자 마음대로.

from bs4 import BeautifulSoup

# 문서가져오기
with open("./rpabasic/crawl/beautifulsoup/story.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, "lxml")

# 타이틀 클래스명 가진 태그 요소 가져오기
title = soup.select_one("p.title")  # .title = class가 title
# print(title)
# print(title.get_text())

# id가 link1인 태그 요소 가져오기
link1 = soup.select_one("#link1")  # #link1 = id가 link1
# print(link1)
# print(link1.get_text())
# print(link1.string)

# data-* 속성 태그요소 가져오기
link2 = soup.select_one("a[data-io='tillie']")
# print(link2)
# print(link2.get_text())

# p클래스 안에 자식 태그 a 모두 가져오기
all_a = soup.select("p.story > a")  # > : 자식
# print(all_a) # find_all , select : 리스트 형식
for link in all_a:
    print(link)
    print(link.get_text())
