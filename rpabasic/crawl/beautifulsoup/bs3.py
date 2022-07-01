from bs4 import BeautifulSoup

# 문서 가져오기
with open("./rpabasic/crawl/beautifulsoup/story.html", "r") as f:
    html = f.read()
    # print(html)

soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# 1. 태그명으로 찾기
# title = soup.title
# print("title : {}".format(title))
# print(f"title : {title}")  # format을 앞에 f붙여서 사용할 수 있다.
# print("title 내용 : {}".format(title.get_text()))
# print("title 부모 태그 : {}".format(title.parent))

# h1 태그 찾기
# h1 = soup.h1
# print("h1 : {}".format(h1))
# print("h1 내용 : {}".format(h1.get_text()))
# print("h1 부모태그 : {}".format(h1.parent))

# p태그 찾기
p1 = soup.p

print(soup.p)  # 첫번째 만나는 p태그 출력
print("p : {}".format(p1))
print()

print(soup.p.get_text())  # p태그 내용 출력
print("p 내용 : {}".format(p1.get_text()))
print()

print(soup.p.attrs)  # p 태그 속성들
print("p태그 속성들 : {}".format(p1.attrs))
print()

print(soup.p["class"])  # p 태그 class 출력
print("p태그 class명 : {}".format(p1["class"]))
