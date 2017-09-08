import requests
from bs4 import BeautifulSoup
'''
1. 下载https://en.wikipedia.org/wiki/Machine_translation 页面的内容并保存为mt.html

       需要编写代码来下载页面。

2. 统计mt.html中<p>标签内下所有单词以及数目并存储到mt_word.txt中。

       mt_word.txt有如下几点要求：

       a) 每个单词一行。单词在前，单词出现的次数在后，中间用Tab(\t)进行分隔。

       b) 单词要按照单词数目从多到少的顺序进行排列。比如说单词a出现了100次，单词b出现了10次，则单词a要在单词b的前面。

3. 提取出mt.html中所有的年份信息（比如说页面中的1629, 1951这些的四位数字就是年份）存储到mt_year.txt中。

       mt_year.txt有如下几点要求：

       a) 每个年份是一行。

       a) 年份需要从过去到现在的顺序进行排列。比如说文章中出现了2007和1997，则1997需要排在2007的前面。
'''
#1
req=requests.get('https://en.wikipedia.org/wiki/Machine_translation').content
html=req.decode('UTF-8')
file=open('mt.html',mode='w',encoding='UTF-8')
file.write(html)

#2
soup=BeautifulSoup(html,'lxml')
p=soup.find_all('p')
for pp in p:
    print(pp.get_text())


