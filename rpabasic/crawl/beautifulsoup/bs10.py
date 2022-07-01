import requests
from bs4 import BeautifulSoup

url = "https://pythonscraping.com/pages/page3.html"
res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")

# h1 태그 가져오기
h1 = soup.select_one("h1")
# print(f"h1 태그 : {h1.get_text()}")

# 상단 내용 가져오기
content = soup.select_one("div#content")
# print(f"content : {content.get_text()}")

# 모든 img 태그 가져오기
img_list = soup.find_all("img")
# print(f"img_list : {img_list}")

# 타이틀 행 가져오기
row = soup.select("table#giftList>tr:nth-child(1)")
# print(row)
# for item in row:
#     print(item.get_text())

# 테이블 내용 가져오기
table = soup.find("table", id="giftList")
# print(table.get_text())

# 가격만 가져오기
cost_list = soup.select("tr.gift")
for cost in cost_list:
    print(cost.find_all("td")[2].get_text())  # 3번쨰 td
