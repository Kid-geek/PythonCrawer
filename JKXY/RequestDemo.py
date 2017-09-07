import requests

# html=requests.get('http://www.douban.com').content
# print(html.decode())

f=open('deep.png','rb')
data={'smfile':f}
content=requests.post('https://sm.ms/api/upload',data).content
print(content.decode())
f.close()