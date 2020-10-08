import requests

# 忽略verify=False的警告，方式1
from requests.packages import urllib3
urllib3.disable_warnings()

# 忽略verify=False的警告，方式2
# import logging
# logging.captureWarnings(True)

#r = requests.get('https://static2.scrape.cuiqingcai.com')

# verify=False：不验证ssl证书
r = requests.get('https://static2.scrape.cuiqingcai.com', verify=False) 
# 可以指定一个本地证书用作客户端证书
#r = requests.get('https://static2.scrape.cuiqingcai.com', cert=('/path/server.crt', '/path/server.key')) 
print(r.status_code)
