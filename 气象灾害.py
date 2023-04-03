import re
import requests
from bs4 import BeautifulSoup
import time
import json

urls = []  # 存放标题
txt_name = "气象灾害具体内容14.txt"  # 文件名
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'}

with open(txt_name, 'w', encoding='utf-8') as f:  # 创建文件
    f.write(txt_name + '\r')  # 写入文件名
    f.close()
    # 54-64   ?_=1655976291954
    # for i in range(54,65):#遍历关键词的页数
    url1 = "http://news.weather.com.cn/"
    resp1 = requests.get(url1, headers=headers)  # 建立链接
    resp1.encoding = 'utf-8'  # 读取中文时不会出现乱码
    url = "http://www.weather.com.cn/pubm/news2019_more.htm?callback=jsonpcallback"
    resp = requests.get(url, headers=headers)  # 建立链接
    resp.encoding = 'utf-8'  # 读取中文时不会出现乱码
    c2_result = re.findall('"c2":"(.*?)"', resp.text)
    for i in c2_result:
        # print(i)
        urls.append(i)
    content = resp1.text
    # print(content)
    bs = BeautifulSoup(content, 'html.parser')  # 解析文档，用html的解析器
    for news in bs.select('.newcardlist'):
        url = news.select('a')[0]['href']  # 提取文章出链接
        urls.append(url)
        # print(url)
    for news in bs.select('.newcardtitle'):
        url = news.select('a')[0]['href']  # 提取文章出链接
        urls.append(url)
        # print(url)
    '''
    for news in bs.select('.oneimgnews_right'):
        url = news.select('a')[0]['href']  # 提取文章出链接
        urls.append(url)
        print(url)
    for news in bs.select('.noimgnews zxcard'):
        url = news.select('a')[0]['href']  # 提取文章出链接
        urls.append(url)
        print(url)
    '''
for i in range(len(urls)):  # 遍历每篇文章的链接
    resp = requests.get(urls[i], headers=headers)
    resp.encoding = 'utf-8'
    content = resp.text
    bs = BeautifulSoup(content, 'html.parser')  # 解析文档，用html的解析器
    top_title = bs.select('.articleTOP p')
    for tex in top_title:
        title = tex.get_text()
        with open(txt_name, 'a', encoding='utf-8') as f:  # 写入刚刚建立的txt文件
            f.write(title)
            f.close()
    for text in bs.select('.articleBody p'):
        content = text.get_text()
        print(content)
        with open(txt_name, 'a', encoding='utf-8') as f:  # 写入刚刚建立的txt文件
            f.write(content)
            f.close()
    for con in bs.select('.tqgb-content p span b'):
        conn = con.get_text()
        print(con)
        with open(txt_name, 'a', encoding='utf-8') as f:  # 写入刚刚建立的txt文件
            f.write(content)
            f.close()
    for con in bs.select('.tqgb-content p'):
        conn = con.get_text()
        print(con)
        with open(txt_name, 'a', encoding='utf-8') as f:  # 写入刚刚建立的txt文件
            f.write(content)
            f.close()

# print("txt文件已经成功记录！")
