import requests
import logging
import re
import pymongo
import multiprocessing
from pyquery import PyQuery as pq
from urllib.parse import urljoin
from mongo_client import client

logging.basicConfig(level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://static1.scrape.cuiqingcai.com'
TOTAL_PAGE = 10
db = client['movies']
collection = db['movies']

# 页面爬取
def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == requests.codes.ok:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 列表页爬取
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

# 解析列表页
def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info('get detail url %s', detail_url)
        yield detail_url

# 详情页爬取
def scrape_detail(url):
    return scrape_page(url)

# 详情页解析
def parse_detail(html):
    doc = pq(html)
    cover = doc('img.cover').attr('src')
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) if published_at and re.search('(\d{4}-\d{2}-\d{2})', published_at) else None
    drama = doc('.drama p').text()
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
            'cover': cover,
            'name': name,
            'categories': categories,
            'published_at': published_at,
            'drama': drama,
            'score': score,
            }

# 保存到MongoDB
def save_data(data):
    collection.update_one({
        'name':data.get('name')
        }, {
            '$set':data
            }, upsert=True)
# 串联调用
def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data)
        logging.info('saving data to mongodb')
        save_data(data)
        logging.info('data saved successfully')

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
