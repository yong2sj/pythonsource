from bs4 import BeautifulSoup

# 문서 가져오기
with open("./rpabasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()
    # print(html)

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# 2. find ~~

# 첫번째 p 태그
p1 = soup.find("p")  # soup.find("p",class_="title")
print(p1)
print()

p2 = soup.find("p", class_="story")  # 형제 요소 찾기 보다 유용
# print(f"p 두번째 : {p2}")
# print(f"p 두번째 내용 : {p2.get_text()}")
# print(f"p 두번째 속성들 : {p2.attrs}")
# print(f"p 두번째 특정 속성값(class명) : {p2['class']}")
# *** 속성값 : id, class, href ..... ***

# 클래스명이 동일해서 못찾으므로 형제방식으로 찾음
p3 = p2.find_next_sibling("p")

# print(f"p 세번째 : {p3}")
# print(f"p 세번째 내용 : {p3.get_text()}")
# print(f"p 세번째 속성들 : {p3.attrs}")
# print(f"p 세번째 특정 속성값(class명) : {p3['class']}")

# 첫번째 a
a1 = soup.find("a")

# 두번째 a
a2 = soup.find("a", id="link2")
# print(f"a 두번째 : {a2}")
# print(f"a 두번째 내용 : {a2.get_text()}")
# print(f"a 두번째 속성들 : {a2.attrs}")
# print(f"a 두번째 특정 속성값(class명) : {a2['id']}")

# 세번째 a
a3 = soup.find("a", id="link3")
a3 = soup.find("a", id="link3", class_="sister")
a3 = soup.find("a", attrs={"class": "sister", "id": "link3", "data-io": "tillie"})
# print(f"a 세번째 : {a3}")
# print(f"a 세번째 내용 : {a3.get_text()}")
# print(f"a 세번째 속성들 : {a3.attrs}")
# print(f"a 세번째 특정 속성값 : {a3['id']}")

# findall
# a = soup.find_all("a")
# print(a)  # 리스트 형식으로 출력됨(하나여도 리스트형식으로 출력)

# b = soup.find_all("b")
# print(b)

# limit : 개수 지정해서 가져오기
# a = soup.find_all("a", limit=2)
# print(a)

# a = soup.find_all("a", class_="sister")
# print(a)

# string만 찾아 출력
a = soup.find_all(string=["Elsie", "Lacie"])
print(a)
