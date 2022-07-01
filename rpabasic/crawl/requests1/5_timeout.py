import requests

url = "https://api.github.com/events"

res = requests.get(url, timeout=0.001)  # timeout 시간동안 응답안오면 error처리
print(res.text)
