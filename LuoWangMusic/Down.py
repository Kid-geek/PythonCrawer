from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve


number=input('输入页码:')
root_url = 'http://www.luoo.net/tag/?p=' + str(number)
html = requests.get(root_url).content.decode()
issues_soup = BeautifulSoup(html, 'lxml')
issues = issues_soup.find_all('div', class_='item')
issue_dict = {}
issue_url_list = []
issue_name_list = []
issue_like_list = []
for issue in issues:
    issue_soup = BeautifulSoup(str(issue), 'lxml')
    issue_url = issue_soup.a.get('href')
    print( '期次链接:'+issue_url)
    # print(issue_url)
    # print(issue_xihuan)
urlretrieve('http://mp3-cdn2.luoo.net/low/luoo/radio947/03.mp3',filename='03.mp3')