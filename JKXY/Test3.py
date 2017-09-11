from urllib import request
import re

captcha_url = 'https://account.guokr.com/sign_in/?success=https%3A%2F%2Faccount.guokr.com%2Foauth2%2Fauthorize%2F%3Fclient_id%3D32353%26redirect_uri%3Dhttp%253A%252F%252Fwww.guokr.com%252Fsso%252F%253Flazy%253Dy%2526rid%253D3893804033%2526success%253Dhttp%25253A%25252F%25252Fwww.guokr.com%25252F%26response_type%3Dcode%26state%3D9e3cdc6fe4a3f3623229745400e934efa70058156e05ffad7897476063acf469--1505099690%26suppress_prompt%3D1'

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3387.400 QQBrowser/9.6.11984.400',
          }

res=request.urlopen(captcha_url).read().decode()
imgurl=re.findall('<img src="(.*?)" id="captchaImage"',res)[0]

print(imgurl)



