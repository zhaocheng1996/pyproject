import requests
from urllib.parse import urlencode
from requests.exceptions import RequestException
import json
from bs4 import BeautifulSoup
import re


#获取索引页
def get_page_index(offset,keyword):
    data = {
    'offset': offset,
    'format': 'json',
    'keyword': keyword,
    'autoload': 'true',
    'count': '20',
    'cur_tab': 1
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code == 200:
           return response.text
           print(response.status_code)
        return  None
    except RequestException:
        print('请求索引页出错')
        return None

def parse_page_index(html):
    data = json.loads(html)#json.load会转变成一个对象
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_page_detail(url):
    try:
        response = requests.get(url)
        print("aaaaa")
        if response.status_code == 200:
           return response.text
           #print(response.status_code)
        return  None
    except RequestException:
        print('请求详情页出错',url)
        return None

#解析详情页信息,网站源代码，发现图片集的url都在gallery键的值中
def parse_page_detail(html):
    soup = BeautifulSoup(html, 'lxml')
    #title = soup.select('title')[0].get_text()
    #print(title)
    images_position = re.compile('var gallery =(.*?);',re.S)
    result = re.search(images_position,html)
    if result:
        print(result.group(1))

def main():
    html=get_page_index(0,'街拍')
    #print(html)
    for url in parse_page_index(html):
        #print(url)
        html=get_page_detail(url)
        if html:
            parse_page_detail(html)

if __name__ == '__main__':
    main()

