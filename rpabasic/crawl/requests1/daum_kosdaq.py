from fake_useragent import UserAgent
import csv
import requests

headers = {"User-agent": UserAgent().chrome, "referer": "https://finance.daum.net"}
path = "./rpabasic/crawl/download/"
data = []

try:
    userAgent = UserAgent()

    url = "https://finance.daum.net/api/search/ranks?limit=10"
    # 위 url 접속 : 403 Forbidden
    # sol : referer 주소 넣어서 가져와야함
    res = requests.get(url, headers=headers)
    print(res)

    rank_json = res.json()["data"]

    for item in rank_json:
        print(
            "순위 {}, 금액 {}, 회사명 {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )

except Exception as e:
    print(e)
