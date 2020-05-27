# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


# 解析页面
def html_parse():
    for url in get_page():
        resp = requests.get('https://book.douban.com/top250?start=0')
        # 设置一个soup对象
        soup = BeautifulSoup(resp.text, 'lxml')
        # 获取书名
        alldiv = soup.find_all('div', class_='pl2')
        names = [div.find('a')['title'] for div in alldiv]
        # 获取作者
        allp = soup.find_all('p', class_='pl')
        authors = [p.text.split('/')[0] for p in allp]
        # 评分
        starspan = soup.find_all('span', class_='rating_nums')
        scores = [s.get_text() for s in starspan]
        # 简介
        sumspan = soup.find_all('span', class_='inq')
        sums = [i.get_text() for i in sumspan]
        # 保存数据
        for name, author, score, sum in zip(names, authors, scores, sums):
            data = str(name) + '#' + str(author) + '#' + str(score) + '#' + str(sum)
            # 保存数据
            f.writelines(data + '\n')


# 获取所有页面url
def get_page():
    baseurl = 'https://book.douban.com/top250?start={}'
    urllist = []
    for i in range(10):
        a = i * 25
        url = baseurl.format(a)
        urllist.append(url)
    return (urllist)


# 保存文件
f = open('豆瓣图书Top250.txt', 'w', encoding='utf-8')
# 调用函数
html_parse()
f.close()
