from urllib.request import urlopen, Request
from fake_useragent import UserAgent

url = "https://sports.news.naver.com/news?oid=411&aid=0000011567"
try:
    userAgent = UserAgent()
    headers = {"User-agent": userAgent.chrome}

    reqeust_url = Request(url, headers=headers)
    res = urlopen(reqeust_url).read().decode("utf-8")
    # print(res)
    print(reqeust_url.header_items())
    # [('Host', 'sports.news.naver.com'), ('User-agent', 'Python-urllib/3.10')]
    # pip install fake-useragent
except Exception as e:
    print(e)
