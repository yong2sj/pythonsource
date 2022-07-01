import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://n.news.naver.com/article/214/0001206348?cds=news_media_pc&type=editn"

# ConnectionError(err, request=request)
headers = {"user-agent": UserAgent().chrome}

res = requests.get(url, headers=headers)

# print(res.text)

soup = BeautifulSoup(res.text, "lxml")

# 특정 엘리먼트 찾기 - 1. 태그 이용(가장 처음에 만나는 태그만 가져옴)
print(soup.h2)

# 특정 엘리먼트 찾기 - 2. find(), find_all(), find_*()
h2_element = soup.find("h2", class_="media_end_head_headline")
print(h2_element)
