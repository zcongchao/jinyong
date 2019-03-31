# -*- coding: utf-8 -*-
import sys 
stdi,stdo,stde=sys.stdin,sys.stdout,sys.stderr
reload(sys) # Python2.5 初始化后删除了 sys.setdefaultencoding 方法，我们需要重新载入
sys.stdin,sys.stdout,sys.stderr=stdi,stdo,stde
sys.setdefaultencoding('utf-8') 
import os, codecs
import	jieba
from collections import Counter

class WordFrequency:
    @staticmethod
    def statistic(namelist,namelist_1,namelist_2,namelist_3,text):
        result = [0] * (len(namelist))
        seg_list = jieba.cut(text)
        c = Counter()
        for x in seg_list:
			if len(x)>1 and x != '\r\n':
				c[x] += 1

        for (key,value) in c.items():
            k = "%s" % (key)
            v = int(value)

            if k.decode('utf-8') in namelist:
				num = namelist.index(k.decode('utf-8'))
				result[num] = result[num] + v
				#print namelist[num - 1] 
            elif k.decode('utf-8') in namelist_1:
				num = namelist_1.index(k.decode('utf-8'))
				result[num] = result[num] + v
            elif k.decode('utf-8') in namelist_2:
				num = namelist_2.index(k.decode('utf-8'))
				result[num] = result[num] + v
            elif k.decode('utf-8') in namelist_3:
				num = namelist_3.index(k.decode('utf-8'))
				result[num] = result[num] + v
            else:
				continue

        return result

