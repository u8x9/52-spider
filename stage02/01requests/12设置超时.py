import requests

r = requests.get('https://httpbin.org/get', timeout=1) # 超时时间：1秒
print(r.status_code)
