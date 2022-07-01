import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 1차 카테고리 추출하기
# category = soup.find_all("a", class_="link__1depth-item", limit=9)
# for item in category:
#     print(item.get_text())

# 2차 카테고리 추출하기
# category2 = soup.find_all("a", class_="link__2depth-item", limit=69)
# for item in category2:
#     print(item.get_text())
# get_text : 태그가 가지고 있는 모든 문자열(자식태그 포함)
# string : 태그가 가지고 있는 문자열만 가져오기

category2 = soup.find_all("li", class_="list-item__2depth", limit=69)
for item in category2:
    href = item.find("a")["href"]
    print(item.get_text(), href)
