import requests
import re
import os

url='https://account.guokr.com/sign_in/?success=https://account.guokr.com/oauth2/authorize/?client_id=32353&redirect_uri=http://www.guokr.com/sso/?lazy=y&rid=3893804033&success=http%3A%2F%2Fwww.guokr.com%2F&response_type=code&state=9e3cdc6fe4a3f3623229745400e934efa70058156e05ffad7897476063acf469--1505099690&suppress_prompt=1'

data={
    'username':'17777784690',
    'password':'zh280705132',
    'permanent':'y'
}

session=requests.Session()
req=session.get(url).content.decode()
imgurl=re.findall('<img src="(.*?)" id="captchaImage"',req)[0]
captchaRand=re.findall('id="captchaRand" value="(.*?)">',req)[0]
csrf_token=re.findall('name="csrf_token" type="hidden" value="(.*?)">',req)[0]

data['captcha_rand']=captchaRand
data['csrf_token']=csrf_token

with open('yanzhengma.png','wb') as f:
    f.write(requests.get(imgurl).content)
f.close()
os.startfile('yanzhengma.png')
yanzheng=input('验证码：')
data['captcha']=yanzheng

result_url='http://www.guokr.com/settings/profile/'

login_url='https://account.guokr.com/sign_in/?success=https%3A%2F%2Faccount.guokr.com%2Foauth2%2Fauthorize%2F%3Fclient_id%3D32353%26redirect_uri%3Dhttp%253A%252F%252Fwww.guokr.com%252Fsso%252F%253Flazy%253Dy%2526rid%253D2205379977%2526success%253Dhttp%25253A%25252F%25252Fwww.guokr.com%25252F%26response_type%3Dcode%26state%3D7f22c5704fcd120dda92d06d69375fbc3d021def8def40538081cee20eb53b44--1505100834%26suppress_prompt%3D1'

result=session.post(login_url,data=data).content.decode()
resss=session.get(result_url).content.decode()
print(resss)


