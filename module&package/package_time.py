# coding:utf-8

import time #导入time包
import datetime #导入datetime包
#datetime更多的是对于日期的处理 time更多是对于时间的处理

now = time.time() #time包里的time函数：生成时间戳函数。 返回秒级别的浮点类型
print("1",now, type(now))

time_obj = time.localtime(now) #获得本地时间函数，传入参数时间戳（可不传）
print("2",time_obj, type(time_obj))
#time.sleep(5) #time包中的sleep暂停函数 休眠5秒
current_time_obj = time.localtime()
print("3",current_time_obj,type(current_time_obj))

before = now - 100000 #修改时间戳-100000s
before_time_obj = time.localtime(before)
print("4",before_time_obj)

print("5",time.time() * 1000) #时间戳 秒转换毫秒
print("6",time.time())#时间戳 秒

#for i in range(10): #测试暂停函数 每循环一次就暂停一秒
#     print(i)
#     time.sleep(1)

datetime_now = datetime.datetime.now()
datetime_timestamp = datetime.datetime.timestamp(datetime_now) #datetime的生成时间戳函数 注意括弧内必须传入参数
print("7",'datetime 生成的时间戳 %s' % datetime_timestamp)

datetime_obj = datetime.datetime.fromtimestamp(datetime_timestamp) #datetime中时间戳转时间对象函数fromtimestamp
print("8",datetime_obj)
