from urllib import request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    target_url='http://www.biqukan.com/2_2822'
    head={}
    head['User-Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    target_req=request.Request(target_url,headers=head)
    target_res=request.urlopen(target_req)
    target_html=target_res.read().decode('gbk','ignore')
    listmain_soup=BeautifulSoup(target_html,'lxml')
    chapters=listmain_soup.find_all('div',class_='listmain')
    print(str(chapters))
    download_soup=BeautifulSoup(str(chapters),'lxml')
    begin_falg=False
    for child in download_soup.dl.children:
        if child != '\n':
            if child.string==u'《雪中悍刀行》正文卷':
                begin_falg=True
            if begin_falg==True and child.a!=None:
                download_url='http://www.biqukan.com'+child.a.get('href')
                download_name=child.string
                print(download_name+':'+download_url)


