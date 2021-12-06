# coding:utf-8

from datetime import datetime  #from 包 import 模块 后面的datetime是模块名（注意还有一种导入包的写法是import datetime 这里的datetime就是包了）
from datetime import timedelta #注意这个timedelta不是模块 而是函数（原因不必深究） 原因可能是1.timedelta直接写在了datetime包的__init__模块里2.__init__模块提前导入了timedelta函数

now = datetime.now()
print("1",now, type(now))
now_str = now.strftime('%Y-%m-%d %H:%M:%S') #时间转字符串
print("2",now_str, type(now_str))
now_obj = datetime.strptime(now_str, '%Y-%m-%d %H:%M:%S') #字符串又转回时间
print("3",now_obj, type(now_obj), '----')

three_days = timedelta(days=3)
after_three_day = now + three_days
print("4",after_three_day)
after_three_day_str = after_three_day.strftime('%Y/%m/%d %H:%M:%S')
print("5",after_three_day_str, type(after_three_day_str))
after_three_day_obj = datetime.strptime(after_three_day_str, '%Y/%m/%d %H:%M:%S')
print("6",after_three_day_obj, type(after_three_day_obj), '----')

before_three_day = now - three_days
print("7",before_three_day)
before_three_day_str = before_three_day.strftime('%Y%m%d')
print("8",before_three_day_str, type(before_three_day_str))
before_three_day_obj = datetime.strptime(before_three_day_str, '%Y%m%d')
print("9",before_three_day_obj, type(before_three_day_obj), '-----')

one_hour = timedelta(hours=1)
before_one_hour = now - one_hour
print("10",before_one_hour)
before_one_hour_str = before_one_hour.strftime('%H:%M:%S')
print("11",before_one_hour_str, type(before_one_hour_str))

#default_str = '2020 12 abc'  #这两行报错 abc不能匹配
#print(datetime.strptime(default_str, '%Y %m'))


