# pip install 'requests[socks]'
import requests

proxies = {
        'http':'socks5://user:passwd@host:port',
        'https':'socks5://user:passwd@host:port',
        }
requests.get('https://httpbin.org/get', proxies=proxies)
