from bs4 import BeautifulSoup

# 문서 가져오기
with open("./rpabasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()
    # print(html)

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# 2. find ~~

# 첫번째 p 태그
p1 = soup.find("p", "title")  # soup.find("p",class_="title")
print(p1)
print()

# 형제 p 태그 찾기
p2 = p1.find_next_sibling("p")  # 다음 형제
# print(f"p 두번째 : {p2}")
# print(f"p 두번째 내용 : {p2.get_text()}")
# print(f"p 두번째 속성들 : {p2.attrs}")
# print(f"p 두번째 특정 속성값(class명) : {p2['class']}")

# p3 = p2.next_sibling.next_sibling
p3 = p2.find_next_sibling("p")
# print(f"p 세번째 : {p3}")
# print(f"p 세번째 내용 : {p3.get_text()}")
# print(f"p 세번째 속성들 : {p3.attrs}")
# print(f"p 세번째 특정 속성값(class명) : {p3['class']}")

# 첫번째 a
a1 = soup.a

# 두번째 a
a2 = a1.find_next_sibling("a")
# print(f"a 두번째 : {a2}")
# print(f"a 두번째 내용 : {a2.get_text()}")
# print(f"a 두번째 속성들 : {a2.attrs}")
# print(f"a 두번째 특정 속성값(class명) : {a2['id']}")

# p1 = p2.find_previous_sibling("p")  # 앞쪽 p태그 찾기

for v in p2.next_element:  # p2위치에서 다음 요소 나옴
    print(v, end="")
