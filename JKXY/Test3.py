def get_days(month):
    if month == '1':
        days=22
        return days
    elif month == '2':
        days = 20
        return days
    elif month == '3':
        days = 23
        return days
    elif month == '4':
        days = 20
        return days
    elif month == '5':
        days = 22
        return days
    elif month == '6':
        days = 23
        return days
    elif month == '7':
        days = 21
        return days
    elif month == '8':
        days = 23
        return days
    elif month == '9':
        days = 21
        return days
    elif month == '10':
        days = 22
        return days
    elif month == '11':
        days = 22
        return days
    elif month == '12':
        days = 21
        return days
if __name__ == '__main__':
    month=input('输入月份:')
    days=get_days(month)
    leave=input('输入请假天数：')
    work=days-(int(leave))
    shui = (int(work) * 120 - 800) * 0.2
    gongzi = int(work) * 120 - shui
    shuiqian = int(work) * 120
    print('工作天数：%s  税前工资:%s  税后工资:%s  税钱:%s ' % (work,shuiqian, gongzi, shui))
    input('结束')