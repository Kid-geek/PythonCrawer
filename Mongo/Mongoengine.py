from mongoengine import *

connect('mydb')


class Test(Document):
    name=StringField(required=True)
    age=IntField(required=True)
    sex=StringField(required=True)
# 添加
# zhhh=Test('zhhh',11,'nan')
# zhhh.save()

# 查询
find=Test.objects()
for each in find:
    print(each.name)
#详细查询
find2=Test.objects(sex='nan')
for each in find2:
    print(each.name)

#删除
delect=Test.objects(name='zhhh')
delect.delete()

