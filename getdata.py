#-*- coding: utf-8 -*-
#coding=gbk
import urllib.request
from bs4 import BeautifulSoup
import re

link_standard = re.compile(r'<a href="(.*)">')                           #影片链接规则
img_standard = re.compile(r'class="" src="(.*)" width="100"/>', re.S)                   #影片海报
name_standard = re.compile(r'<span class="title">(.*)</span>')                    #影片片名
score_standard = re.compile(r'property="v:average">(.*?)</span>', re.S)    #影片得分
bodys_standard = re.compile(r'<span>(\d*)人评价</span>', re.S)                                 #评价人数
summary_standard = re.compile(r'<span class="inq">(.*)</span>', re.S)                         #影片概况
inf_standard = re.compile(r'<p class="">(.*?)</p>', re.S)    #影片信息


def get_one_page(url):
    #爬取每页数据
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137'
    req = urllib.request.Request(url, headers=headers)
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        return html
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
        return "未获取指定数据"


def get_data(base_url):
    #爬取所有数据
    all_data = []
    for i in range(0, 10):
        html = get_one_page(base_url + str(i*25))
        content = BeautifulSoup(html, "html.parser")
        for each_movie in content.find_all("div", class_="item"):
            data = []  # 建立data列表，存放单部电影数据
            each_movie = str(each_movie)

            link = re.findall(link_standard, each_movie)[0]    #影片链接
            data.append(link)

            img = re.findall(img_standard, each_movie)[0]  #影片海报
            data.append(img)

            name = re.findall(name_standard, each_movie)  #影片片名
            if len(name) == 2:
                inname = name[0]
                data.append(inname)
                outname = name[1][3:]
               #print(outname, "***********************")
                data.append(outname)
            else:
                data.append(name[0])
                data.append(" ")    #留空值占位，保持格式统一

            score = re.findall(score_standard, each_movie)[0]  #影片得分
            data.append(score)

            bodys = re.findall(bodys_standard, each_movie)[0]  #评价人数
            data.append(bodys)

            summary = re.findall(summary_standard, each_movie)  #内容概况
            if len(summary) != 0:
                data.append(summary[0].replace("。", ""))
            else:
                data.append(" ")    #留空占位

            inf = re.findall(inf_standard, each_movie)[0]    #影片信息
            inf = inf.replace("...<br/>", " ")
            inf = inf.replace("/", "  ")
            inf = inf.strip()
            data.append(inf)
            all_data.append(data)
    return all_data