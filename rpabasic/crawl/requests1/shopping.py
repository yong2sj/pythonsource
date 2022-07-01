import requests

url = "https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1656656937783"

# 순위, 제품명
res = requests.get(url)
# print(res.text)

for idx, item in enumerate(res.json(), 1):  # idx 사용시 enumerate 필수
    print(idx, item["product_name"])
