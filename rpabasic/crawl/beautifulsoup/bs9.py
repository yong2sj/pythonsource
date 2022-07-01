import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"

res = requests.get(url)
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 사진 저장
# 요소찾기 -> copy -> copy selector
# #mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
img1 = soup.select_one(
    "#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img"
)
# print(img1)
# print()
# print(img1["src"])

# 이미지 다운로드 - urlretrieve

path = "./rpabasic/crawl/download/"

# urlretrieve("이미지 원본 경로", "다운로드 받을 경로")
# urlretrieve("http:" + img1["src"], path + "subway1.jpg")

# 두 번째 사진 저장
# #mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img
img2 = soup.select_one("#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img")

urlretrieve("http:" + img2["src"], path + "subway2.jpg")