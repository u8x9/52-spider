import requests

data = {'name': 'u8x9', 'age': 99}
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", }

r = requests.post('https://httpbin.org/post', data=data, headers=headers)
print(r.text)
