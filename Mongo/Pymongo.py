from pymongo import MongoClient
client=MongoClient()
database=client.mydb
col=database.test
# 插入
# info_dict={'name':'jike','age':33,'sex':'nv'}
# col.insert(info_dict)

# 查询
# zh=col.find({'name':'zhh'})
# for each in zh:
#     print(each['age'])

# 更新
# col.update({'name':'zhh'},{'$set':{'age':'90'}})

# 删除
# col.delete_many({'name':'zhh'})
for each in col.find().limit(2).skip(1):
    print(each)