import requests

r = requests.get('http://www.baidu.com')
print(r.cookies)

for k, v in r.cookies.items():
    print(f'{k} = {v}')
