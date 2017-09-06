from bs4 import BeautifulSoup
import requests
import re

one=[]
two=[]
three=[]
fore=[]
five=[]
six=[]

def get_url():
    url='https://movie.douban.com/subject/24753477/comments?start=0&limit=20&sort=new_score&status=P'
    req = requests.get(url)
    req.encoding = 'utf-8'
    html = req.text
    soup = BeautifulSoup(html, 'lxml')
    div = soup.find_all('div', class_='center')
    a_soup = BeautifulSoup(str(div), 'lxml')
    aa = a_soup.find_all('a', class_='next')
    for aaa in aa:
        real_url = 'https://movie.douban.com/subject/24753477/comments' + aaa.get('href')
        print(real_url)
    return real_url


for num in range(3):
    url=get_url()
    print(url)
    req=requests.get(url)
    req.encoding='utf-8'
    html=req.text
    soup=BeautifulSoup(html,'lxml')
    div=soup.find_all('div',class_='comment')
    for divv in div:
        regex='<span class="allstar[\s\S]{0,11}title="([\s\S]{0,2})"'
        pingjia=re.findall(regex,str(divv))
        if str(pingjia)=="['力荐']":
            five.append(pingjia)
        elif str(pingjia)=="['推荐']":
            fore.append(pingjia)
        elif str(pingjia) == "['还行']":
            three.append(pingjia)
        elif str(pingjia) == "['较差']":
            two.append(pingjia)
        elif str(pingjia) == "['很差']":
            one.append(pingjia)
        else:
            six.append(pingjia)








print("五星:"+str(five.__len__()))
print("四星:"+str(fore.__len__()))
print("三星:"+str(three.__len__()))
print("二星:"+str(two.__len__()))
print("一星:"+str(one.__len__()))
print("其他:"+str(six.__len__()))
    # print("评分："+str(pingjia)+"  影评:"+divv.p.text)
