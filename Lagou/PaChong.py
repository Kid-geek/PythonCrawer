import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)
driver=webdriver.PhantomJS('phantomjs.exe',desired_capabilities=dcap)
driver.get('https://www.lagou.com/jobs/list_%E7%88%AC%E8%99%AB?px=default&gx=%E5%AE%9E%E4%B9%A0&city=%E5%8C%97%E4%BA%AC&isSchoolJob=1#order')
html=driver.page_source
soup=BeautifulSoup(html,'lxml')
company_list=soup.find_all('li',class_='con_list_item default_list')
for company in company_list:
    name=company['data-company']
    money=company['data-salary']
    work=company['data-positionname']

    place_soup=BeautifulSoup(str(company), 'lxml')
    place=place_soup.find('span',class_='add').text

    date_soup = BeautifulSoup(str(company), 'lxml')
    date = date_soup.find(name='span', class_='format-time').text

    advantage_soup=BeautifulSoup(str(company),'lxml')
    advantage=advantage_soup.find(name='div',class_='li_b_r').text

    print('公司名称：'+name+'  薪资:'+money+' 岗位:'+work+'工作地点'+place+' 发布日期:'+date+' 职位优势:'+advantage)
    id = company['data-positionid']
    info_url = 'https://www.lagou.com/jobs/'+id+'.html'
    print('详情页:'+info_url)


# html=html.replace(u'\u2002', u' ').replace('\xa9',' ')
# file=open('html.txt','w')
# file.write(html)
# os.startfile('html.txt')


time.sleep(5)
driver.close()