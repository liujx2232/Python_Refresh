# coding:utf-8
# 关于异常-1  Exception  ZeroDivisionError
#2021-12-05

def upper(str_data):
    new_str = 'None~' #先初始化一下字符串
    try:
        new_str = str_data.upper() #如果进入了try 就会给new_str重新赋值；如果不进入，就会转入except模块
    except Exception as e: #捕获通用异常：无法确定异常的情况下使用的捕获方法
        print('程序出错了:{}'.format(e))
    return new_str

result = upper(1) #出现异常
print('result:', result) #返回初始化的字符串“None~”
print("____________________________")
def test():
    try:
        print('123') #这条能打出来
        1 / 0
        print('hello') #打完123后发现有错误所以这条打不出来
    except ZeroDivisionError as e:  #捕获具体异常：确定异常情况下使用的捕获方法 (这个意思是“0在python中不能被整除”)
        print(e)


test()
print("____________________________")

def test1():
    try:
        print('hello')
        print(name) #name是未定义变量
    except (ZeroDivisionError, NameError) as e: #捕获多个异常的写法 要用元组形式把多个异常类型包裹起来
        print(e)
        print(type(e))
        print(dir(e))

test1()

print("_______________下面是多种异常类型的测试_________________")
class Test(object):
    pass

t = Test()
try:
    t.name
except AttributeError as e:
    print(e)

d = {'name': '小慕'}
try:
    d['age']
except KeyError as e:
    print('没有对应的键：', e)

l = [1, 2, 3]
try:
    l[5]
except IndexError as e:
    print(e)

name = 'dewei'
try:
    int(name)
except ValueError as e:
    print(e)

def test(a):
    return a

try:
    test()
except TypeError as e:
    print(e)
