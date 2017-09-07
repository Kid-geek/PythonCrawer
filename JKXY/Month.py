import time
import datetime
import calendar

myDate = []
t = str(time.strftime('%Y-%m-'))
print(time.strftime)
for i in range(1, 32):
    timeStr = t + str(i)
    try:
        # 字符串转换为规定格式的时间
        tmp = time.strptime(timeStr, '%Y-%m-%d')
        # 判断是否为周六、周日
        if (tmp.tm_wday != 6) and (tmp.tm_wday != 5):
            myDate.append(time.strftime('%Y-%m-%d', tmp))
    except:
        print()
if len(myDate) == 0:
    myDate.append(time.strftime('%Y-%m-%d'))


