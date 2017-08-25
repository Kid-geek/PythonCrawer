from urllib import request
from urllib.parse import quote
from bs4 import BeautifulSoup

# book_name=input("要下载的书名:")
search_url=u'http://zhannei.baidu.com/cse/search?q=雪中&click=1&s=2758772450457967865&nsid='
print(search_url)
head={}
head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
req=request.Request(search_url,headers=head)
res=request.urlopen(req)
html=res.read().decode('utf-8')
print(html)
# book_name_soup=BeautifulSoup(html,'lxml')
# href=book_name_soup.find_all(cope_='title',class_='result-game-item-title-link')
# resule=str(href)
# print(href)
