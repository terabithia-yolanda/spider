#-*- coding: utf-8 -*-
#coding=gbk

import xlwt
import sqlite3

def save_data(target_data, save_path):
    #保存数据
    wb = xlwt.Workbook(encoding="uft-8", style_compression=0)
    ws = wb.add_sheet("豆瓣电影TOP250", cell_overwrite_ok=True)
    col_name = ("序号", "电影详情链接", "海报链接", "影片中文名", "影片外文名", "影片评分", "评价人数", "内容概况", "影片其\
它信息")
    for i in range(0, 9):
        ws.write(0,i,col_name[i])
    for i in range(0, 250):
        ws.write(i+1,0,i+1)
        print("第%d条" % (i+1))
        each_data = target_data[i]
        for t in range(1, 8):
            ws.write(i+1,t,each_data[t-1])
    wb.save(save_path)

def  savedb_data(target_data, db_path):
    init_db(db_path)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    for data in target_data:
        l = len(data)
        for index in range(l):
            if index == 4 or index == 5:
                continue
            else:
                #print(data[index])
                data[index] = '"' + data[index] + '"'
        sql = '''
                insert into movie_top_250(
                movie_link, movie_pic, Chinese_name, foreign_name, score, people_count, movie_summary, other_information)
                values(%s)''' % ",".join(data)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(db_path):
    sql = '''create table movie_top_250
             (
                id integer primary key autoincrement,
                movie_link text,
                movie_pic text,
                Chinese_name varchar,
                foreign_name varchar,
                score numeric,
                people_count numeric,
                movie_summary text,
                other_information text
                );'''
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
