import lxml.html
import requests

# url='http://movie.douban.com/top250'
# req=requests.get(url).content
# html=req.decode()
# selector=lxml.html.fromstring(html)
# content=selector.xpath('//span[@class="title"]/')
# print(content)

test='''
<html>
  <head>
    <title>极客学院</title>
  </head>
  <body>
    <div>
      <a class="web" href="http://www.jikexueyuan.com">极客学院的网址</a>
      <a class="friend" href="http://kingname.info">友情链接</a>
    </div>
  </body>
</html>
'''
selector=lxml.html.fromstring(test)
a=selector.xpath('//a[@class="web"]/@href')
print(a)
