import requests

proxies = {
        'http':'http://127.0.0.1:12345',
        'https':'http://127.0.0.1:12345',
        }
requests.get('https://httpbin.org/get', proxies=proxies)
