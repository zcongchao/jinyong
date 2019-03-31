# -*- coding:utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import lxml
import re
import os

URL = 'http://www.jinyongwang.com/tian/'
URL_Base = 'http://www.jinyongwang.com/'
sessionURL = '/tian/695.html'

respond = urllib2.urlopen(URL)
html = respond.read()
soup = BeautifulSoup(html,'lxml',from_encoding='utf-8')
OringialPath = soup.find_all(class_="mlist")
pattern = re.compile('(?<=href=").*?(?=")')
#print str(OringialPath)
listpath =  re.findall(pattern,str(OringialPath) )
#print listpath


web = URL_Base + sessionURL
respond = urllib2.urlopen(web)
html = respond.read()
pattern = re.compile('(?<=<p>).*?(?=</p>)')
text = re.findall(pattern,str(html) )
for i in text:	
    print i