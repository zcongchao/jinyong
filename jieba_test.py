# -*- coding:utf-8 -*-
from __future__ import print_function, unicode_literals
import jieba

'''
#功能 1：分词
seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

# 搜索引擎模式
seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  
print(", ".join(seg_list))
'''

#功能2：自定义词典补充
import sys
sys.path.append("../")

import jieba.posseg as pseg



test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，在自定义词库中也增加了此词为N类\n"
"「台中」正確應該不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)

words = jieba.cut(test_sent)
print('/'.join(words))

print("="*40)
#加载自定义词库后
jieba.load_userdict("userdict.txt")
jieba.add_word('石墨烯')
jieba.del_word('自定义词')
#jieba.add_word('云计算')
words = jieba.cut(test_sent)
print('/'.join(words))





