from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import json
import csv

headers = {"User-agent": UserAgent().chrome, "referer": "https://finance.daum.net"}
path = "./rpabasic/crawl/download/"
data = []
try:
    userAgent = UserAgent()

    url = "https://finance.daum.net/api/search/ranks?limit=10"
    # 위 url 접속 : 403 Forbidden
    # sol : referer 주소 넣어서 가져와야함
    res = urlopen(Request(url, headers=headers)).read().decode("utf-8")
    # print(res)
    # json => dict
    rank_json = json.loads(res)["data"]

    for item in rank_json:
        print(
            "순위 {}, 금액 {}, 회사명 {}".format(
                item["rank"], item["tradePrice"], item["name"]
            )
        )
        data.append(item)

        with open(path + "finance.txt", "a", encoding="utf-8") as txt, open(
            path + "finance.csv", "a", encoding="utf-8", newline=""
        ) as csvfile:

            # 텍스트 저장
            txt.write(
                "순위 {}, 금액 {}, 회사명 {}\n".format(
                    item["rank"], item["tradePrice"], item["name"]
                )
            )

            # csv 저장
            output = csv.writer(csvfile)
            # 헤더명
            output.writerow(data[0].keys())
            for row in data:
                output.writerow(row.values())  # value 저장

except Exception as e:
    print(e)
