import re
import requests

session=requests.Session()
req=session.get('https://www.zhihu.com',headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'}).content
res=req.decode()
xsrf=re.findall('name="_xsrf" value="(.*?)"/>',res)[0]
print(xsrf)
data={'_xsrf':xsrf,'email':'280705132@qq.com','password':'zh280705132','captcha_type':'cn'}
result=session.post('https://www.zhihu.com/login/email',data=data,headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'})
front_page= session.get('https://www.zhihu.com',headers = { 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20'}).content
xsrf1=re.findall('name="_xsrf" value="(.*?)"/>',front_page.decode())[0]
print(xsrf1)
print(front_page.decode())