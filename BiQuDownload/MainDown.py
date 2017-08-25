from urllib import request
from bs4 import BeautifulSoup
import re
import sys

if __name__ == '__main__':
    file=open('雪中悍刀行.txt','w',encoding='utf-8')
    tatget_url='http://www.biqukan.com/2_2822'
    head={}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req=request.Request(tatget_url,headers=head)
    tatget_res=request.urlopen(target_req)
    tatget_html=tatget_res.read().decode('gbk')
    listmain_soup=BeautifulSoup(tatget_html,'lxml')
    chapters=listmain_soup.find_all('div',class_='listmain')
    zhengwen_soup=BeautifulSoup(str(chapters),'lxml')
    zhengwen_flag=False
    index = 1
    numbers=(len(zhengwen_soup.dl.contents)-1)/2
    for child in zhengwen_soup.dl.children:
        if child!='\n':
            if child.string==u'《雪中悍刀行》正文卷':
                zhengwen_flag=True
            if zhengwen_flag==True and child.a!=None:
                download_url='http://www.biqukan.com/'+child.a.get('href')
                download_req=request.Request(download_url,headers=head)
                download_res=request.urlopen(download_req)
                download_html=download_res.read().decode('gbk','ignore')
                download_name=child.string
                texts_soup=BeautifulSoup(download_html, 'lxml')
                texts=texts_soup.find_all(id='content', class_='showtxt')
                text_soup=BeautifulSoup(str(texts),'lxml')
                write_flag=True
                file.write(download_name+'\n\n')
                for each in text_soup.div.text.replace('\xa0',''):
                    if each=='h':
                        write_flag=False
                    if write_flag==True and each!=' ':
                        file.write(each)
                    if write_flag==True and each=='\r':
                        file.write('\n')
                file.write('\n\n')
                print("已下载:" +str((index / numbers)*100) + '\r')
                index+=1
    file.close()