import redis
# 连接Redis
r=redis.StrictRedis(host='127.0.0.1',port=6379)
#写入
# r.set('key','value')
#获取
print(r.get('key'))

# r.append('key','ooh')#向已有信息后添加字符串
# print(r.get('key'))

print(r.keys())
#删除key
r.delete('key')

print(r.keys())
