from bs4 import BeautifulSoup
from urllib import request
if __name__ == '__main__':
    download_url='http://www.biqukan.com/2_2822/14453824.html'
    head={}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url=download_url, headers=head)
    download_response = request.urlopen(download_req)
    download_html = download_response.read().decode('gbk', 'ignore')
    soup_texts = BeautifulSoup(download_html, 'lxml')
    texts=soup_texts.find_all(id='content',class_='showtxt')
    soup_texts=BeautifulSoup(str(texts),'lxml')
    print(soup_texts.div.text.replace('\xa0',''))