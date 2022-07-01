from urllib.request import urlopen
from urllib.parse import urlencode

api = "https://api.ipify.org"

# url = api + "?" + "format=json"
# 딕셔너리 구조
values = {"format": "json"}

url = api + "?" + urlencode(values)  # 딕셔너리 형태를 url형태로 바꾸자

res = urlopen(url).read().decode("utf-8")
print(res)
