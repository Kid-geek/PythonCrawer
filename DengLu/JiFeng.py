import requests

login_url='http://my.gfan.com/doLogin'
date={
    # 'gotoUrl': 'http://my.gfan.com/',
    'loginName': '280705132@qq.com',
    'password': 'zh280705132'
}


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3387.400 QQBrowser/9.6.11984.400',
          'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, * / *;q = 0.8',
          'Accept-Encoding': 'gzip, deflate, sdch, br',
          'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6'}


session=requests.Session()
html=session.get(login_url,headers=header).content.decode()

#竟然不需要验证码参数？！
# authCodeUrl='http://my.gfan.com/captcha'
# with open('yanzhengma.png','wb') as f:
#     f.write(requests.get(authCodeUrl).content)

# authCode=input('验证码为：')
# date['authCode']='abcd'

result = session.post(login_url, data=date, headers=header).content
print(result.decode())