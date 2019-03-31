# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import lxml
import re
import os

class Spider:
    #构造函数参数分别为小说网址链接、小说编号（1~15）、网站链接；
    def __init__(self,URL,URL_ID,URL_Base):
        self.URL = URL
        self.URL_ID = URL_ID
        self.URL_Base = URL_Base
        self.listpath = None

    #打开小说章节
    def get_seeion(self):#获取小说所有章节链接；
        try:
            respond = urllib2.urlopen(self.URL)
            html = respond.read()
            soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
            OringialPath = soup.find_all(class_="mlist")
            pattern = re.compile('(?<=href=").*?(?=")')
            self.listpath =  re.findall(pattern,str(OringialPath) )	
        except:
            print "Error"

    #获取该章节所有段落，返回数据类型为List
    def get_text(self,sessionURL):
        web = self.URL_Base + sessionURL
        respond = urllib2.urlopen(web)
        html = respond.read()
        pattern = re.compile('(?<=<p>).*?(?=</p>)')
        text = re.findall(pattern,str(html))
        return text