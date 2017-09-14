import redis
# 创建连接池
connection_pool=redis.ConnectionPool(host='127.0.0.1',port=6379,db=0)

def getValue(key):
    server=redis.Redis(connection_pool=connection_pool)
    response=server.get(key)
    return response

def setValue(key,value):
    server=redis.Redis(connection_pool=connection_pool)
    server.set(key,value)
