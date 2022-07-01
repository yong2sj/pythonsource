from urllib.request import urlopen  # 정보를 가져와서 메모리에 저장
from urllib.parse import urlencode  # 파라메터로 인코딩할 수 있게 해줌

param = {"query": "영화"}
url = (
    "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&"
    + urlencode(param)
)

try:
    res = urlopen(url).read().decode("utf-8")
except:
    print("URL Error")
else:
    print(res)
