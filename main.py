#-*- coding: utf-8 -*-
#coding=gbk
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3
import urllib.request
import getdata as gd
import save as sv

link_standard = re.compile(r'<a href="(.*)">')	#影片链接规则
img_standard = re.compile(r'class="" src="(.*)" width="100"/>', re.S)	#影片海报
name_standard = re.compile(r'<span class="title">(.*)</span>')	#影片片名
score_standard = re.compile(r'property="v:average">(.*?)</span>', re.S)	#影片得分
bodys_standard = re.compile(r'<span>(\d*)人评价</span>', re.S)	#评价人数
summary_standard = re.compile(r'<span class="inq">(.*)</span>', re.S)	#影片概况
inf_standard = re.compile(r'<p class="">(.*?)</p>', re.S)	#影片信息

def main():
    #获取基础url，爬取数据并存储数据
    base_url = "https://movie.douban.com/top250?start="
    target_data = gd.get_data(base_url)
    save_path = "豆瓣电影评分TOP250.xls"
    db_path = "movie.db"
    sv.save_data(target_data, save_path)
    sv.savedb_data(target_data, db_path)
    
    


if __name__ == "__main__":
    main()
