import requests

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36", 
        }
r = requests.get('https://static1.scrape.cuiqingcai.com', headers=headers)
print(r.text)
