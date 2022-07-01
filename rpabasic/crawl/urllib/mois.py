# 행정안전부 게시판 목록 가져오기
from urllib.request import urlopen
from urllib.parse import urlencode

# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1014
# https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
# ctxCd 값만 바뀜

url = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))  # 딕셔너리구조. key=value

# print(params)  # [{'ctxCd': 1001}, {'ctxCd': 1012}, {'ctxCd': 1013}, {'ctxCd': 1014}]

try:
    for c in params:
        param = urlencode(c)

        url = url + "?" + param
        print("url {}".format(url))

        data = urlopen(url).read().decode("utf-8")
        print()
        print(data)
except Exception as e:
    print(e)
