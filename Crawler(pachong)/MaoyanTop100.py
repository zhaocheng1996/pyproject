'''
我以霸王别姬为例讲解，我们要爬取的目标内容有 电影排名，电影海报链接，电影名称，主演，上映时间以及评分等 6 个主要内容。
'''
import requests
from multiprocessing import Pool #多进程
from requests.exceptions import RequestException
import re
import json

def get_one_page(url):
    try:#不加头文件会被拒绝请求，状态返回403
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
           return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    # 表达式 .*? 是满足条件的情况只匹配一次，即最小匹配.
    #<dd>匹配结果是<dd> 整个正则的开始标志
    # .*?board-index.*?>(\d+)</i>匹配 <i class="board-index board-index-1">1</i>
    # .*?data-src="(.*?)" 匹配图片路径
    #.* ?name"><a.*?>(.*?)</a>  匹配name
    #   匹配主演star 这个匹配不到不知道为毛
    #.*?releasetime">(.*?)</p> <p class="releasetime">上映时间：1953-09-02(美国)</p>匹配上映时间
    # .*?integer">(.*?)</i>.*? 匹配评分
    # fraction">(.*?)</i>.*?  <i class="fraction">1</i></p>pi匹配排名
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)#加了re.S就可以匹配换行符

    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image': item[1],
            'title': item[2],
            'actor':item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score':item[5]+item[6]
        }
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:#a打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
        f.write(json.dumps(content,ensure_ascii=False)+'\n')   # 也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
        #json.dumps()函数是将一个Python数据类型列表进行json格式的编码（可以这么理解，json.dumps()函数是将字典转化为字符串）
        f.close()

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
    #print(html)



if __name__ == '__main__':
    # for i in range(10):
    #     main(i*10)
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])
