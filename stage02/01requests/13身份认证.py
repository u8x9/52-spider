import requests
from requests.auth import HTTPBasicAuth as hba

r = requests.get('https://static3.scrape.cuiqingcai.com', auth=hba('admin', 'admin'))
print(r.status_code)
