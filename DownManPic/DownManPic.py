from urllib.request import urlretrieve
import requests
import time
from bs4 import BeautifulSoup
import os

#获取首页图片详情页 nums为要下载几页图片  默认为1页
def get_urlSet(nums=1):
    url_set = set()
    for num in range(nums):
        url = 'http://www.shuaia.net/index_%d.html' % (num+2)
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
        }
        req = requests.get(url, headers)
        req.encoding = 'utf-8'
        html = req.text
        html_soup = BeautifulSoup(html, 'lxml')
        div = html_soup.find_all('div', class_='item-img-box')
        # 把链接存入set里 避免有重复链接

        for each in div:
            url_set.add(each.a.get('href'))
    return url_set

#获取图片链接存入列表
def get_imgUrlList(url_set):
    img_urlList = []
    for url in url_set:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110     Safari/537.36'
        }
        req=requests.get(url,headers)
        req.encoding='utf-8'
        html=req.text
        div_soup=BeautifulSoup(html,'lxml')
        div=div_soup.find_all(class_='wr-single-content-list')
        for each in div:
            img_urlList.append('http://www.shuaia.net'+each.img.get('src'))
    return img_urlList

# 下载图片
def downImg(img_urlList):
    if 'images' not in os.listdir():
        os.makedirs('images')
    print("共有"+str(img_urlList.__len__())+'张照片')
    for i,img_url in enumerate(img_urlList):
            urlretrieve(img_url, filename='images/'+str(i+1)+'.jpg')
            print("第"+str(i+1) + ':下载成功')
            if i==img_urlList.__len__()-1:
                print("下载成功")
                break

if __name__ == '__main__':
    # nums为要下载的页面数
    urlSet=get_urlSet(nums=2)
    imgUrlList=get_imgUrlList(urlSet)
    downImg(imgUrlList)