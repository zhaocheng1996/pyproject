#!/usr/bin/env python
#coding=utf-8

'''
    #最终输出的结果显示如下：
    { 
            '北京市':{'朝阳区':[邮编, 区号]} 
            '湖南省':{'郴州市':{'区县':[邮编, 区号]}}
    }
'''

import urllib
from bs4 import BeautifulSoup

ZXS_city_name = ''
ZXS_city_dict = {}
ZXS_city_area = ''
ZXS_city_list = []

ProvinceOrArea_name = ''
ProvinceOrArea_dict = {}
ProvinceOrArea_city_name = ''
ProvinceOrArea_city_dict = {}
ProvinceOrArea_city_area = ''
ProvinceOrArea_city_list = []

results = {}

html = (urllib.urlopen('http://www.ip138.com/post/').read())

soup = BeautifulSoup(html)
# print soup.prettify()     #只能用在print的格式化输出上

def deal_ZXS(province):
    ZXS_city_name = province[0].encode('utf-8')
    global ZXS_city_list
    global ZXS_city_dict
    html_ZXS = urllib.urlopen('http://www.ip138.com'+province[1]).read()
    soup_ZXS = BeautifulSoup(html_ZXS)
    tr_items = (soup_ZXS.select('table[class="t12"]')[0]).select('tr')
    flag = 1
    for item in tr_items:
        if flag == 1:
            flag = 0
            continue
        temp_count = 1
        for item_son in (item.select('td')):
            if temp_count in [1, 4]:
                ZXS_city_area = item_son.get_text().encode('utf-8')
                '''
                #通过写文件说明这里写出去的文件是正确的编码
                with open('aa.txt', 'ab') as f:
                    f.write(ZXS_city_area)
                '''
                #ZXS_city_area = (item_son.string)
                #print type(item_son.get_text().encode('utf-8'))
            if temp_count in [2, 5]:
                ZXS_city_list.append(item_son.get_text().encode('utf-8'))
            if temp_count in [3, 6]:
                ZXS_city_list.append(item_son.get_text().encode('utf-8'))
                #在每一次最后进行添加操作
                ZXS_city_dict[ZXS_city_area] = ZXS_city_list
                #完成添加以后清空
                ZXS_city_area = ''
                ZXS_city_list = []
                
            temp_count += 1
    #最后完成直辖市整个的添加动作，并清空变量
    results[ZXS_city_name] = ZXS_city_dict
    ZXS_city_name = ''
    ZXS_city_dict = {}
                     
    
def deal_ProvinceOrArea(province):
    ProvinceOrArea_name = province[0].encode('utf-8')
    global ProvinceOrArea_city_name
    global ProvinceOrArea_city_dict
    global ProvinceOrArea_city_list
    global ProvinceOrArea_dict
    html_ProvinceOrArea = urllib.urlopen('http://www.ip138.com'+province[1]).read()
    soup_ProvinceOrArea = BeautifulSoup(html_ProvinceOrArea)
    tr_items = (soup_ProvinceOrArea.select('table[class="t12"]')[0]).select('tr')
    flag = 1
    for item in tr_items:
        if flag == 1:
            flag = 0
            continue
        
        if len(item.select('td')) == 1:
            ProvinceOrArea_dict[ProvinceOrArea_city_name] = ProvinceOrArea_city_dict
            ProvinceOrArea_city_name = ''
            ProvinceOrArea_city_dict = {}
            continue
        else:
            if len(item.select('td')) < 6:
                for item_son in item.select('td'):
                    ProvinceOrArea_city_name = item_son.get_text().encode('utf-8')
                    break
                continue
                
            temp_count = 1
            for item_son in (item.select('td')):
                if temp_count in [1, 4]:
                    ProvinceOrArea_city_area = item_son.get_text().encode('utf-8')
                if temp_count in [2, 5]:
                    ProvinceOrArea_city_list.append(item_son.get_text().encode('utf-8'))
                if temp_count in [3, 6]:
                    ProvinceOrArea_city_list.append(item_son.get_text().encode('utf-8'))
                    #在每一次最后进行添加操作
                    ProvinceOrArea_city_dict[ProvinceOrArea_city_area] = ProvinceOrArea_city_list
                    #完成添加以后清空
                    ProvinceOrArea_city_area = ''
                    ProvinceOrArea_city_list = []
                    
                temp_count += 1
    #最后完成整个的添加动作，并清空变量
    results[ProvinceOrArea_name] = ProvinceOrArea_dict
    ProvinceOrArea_dict = {}
    ProvinceOrArea_name = ''
    
for item in (soup.select('#map_86')[0].select('area')):
    province = [item['title'], item['href']]
    if province[1] in ['/10/', '/40/', '/30/', '/20/']:
        # 对直辖市进行处理
        deal_ZXS(province)
    else:
        # 对省自治区处理
        deal_ProvinceOrArea(province)

print (results)
