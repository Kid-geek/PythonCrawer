from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup
import  string
import re

def selectBook(book_name):
    search_url = r'http://zhannei.baidu.com/cse/search?q=' + book_name + '&click=1&s=2758772450457967865&nsid='
    search_url = quote(search_url, string.printable)
    print(search_url)
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    req = request.Request(search_url, headers=head)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    book_name_soup = BeautifulSoup(html, 'lxml')
    div = book_name_soup.find_all('div',class_='game-legend-a')
    a_soup = BeautifulSoup(str(div), 'lxml')
    regex = r"location='([\s\S]*?)'\""
    matches=re.search(regex,str(a_soup))
    # 书本链接为第一个搜索结果
    a_href=matches.group(1)
    print(a_href)
    return str(a_href)

def downTXT(book_name):

    bookList_url = selectBook(book_name)
    file = open(book_name + '.txt', 'w', encoding='utf-8')
    head = {}
    head[
        'User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req=request.Request(bookList_url,headers=head)
    target_res=request.urlopen(target_req)
    target_html=target_res.read().decode('gbk')
    listmain_soup=BeautifulSoup(target_html,'lxml')
    chapters=listmain_soup.find_all('div',class_='listmain')
    zhengwen_soup=BeautifulSoup(str(chapters),'lxml')
    zhengwen_flag=False
    index=1
    numbers=(len(zhengwen_soup.dl.contents)-1)/2
    for child in zhengwen_soup.dl.children:
        if child!='\n':
            if child.string==r'《'+book_name+'》正文卷':
                zhengwen_flag=True
            if zhengwen_flag==True and child.a!=None:
                download_url='http://www.biqukan.com/'+child.a.get('href')
                download_req=request.Request(download_url,headers=head)
                download_res=request.urlopen(download_req)
                download_html=download_res.read().decode('gbk','ignore')
                download_name=child.string
                texts_soup=BeautifulSoup(download_html,'lxml')
                texts=texts_soup.find_all(id='content',class_='showtxt')
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
                print("已下载:" + str((index / numbers) * 100) + '\r')
                index += 1
    file.close()

if __name__ == '__main__':
    book_name = input('要下载的书名:')
    downTXT(book_name)





