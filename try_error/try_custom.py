# coding:utf-8
#关于自定义异常类
#2021-12-05

def test(number):
    if number == 100:
        raise ValueError('number 不可以是100')
    return number

result = test(50)
print(result)
#result = test(100) #报错 因为没设置捕获


def test2(number):
    try:
        return test(number)
    except ValueError as e: #设置捕获
        return e

result = test2(100)
print(result)


def test3():
    raise '错误了' #这个写法就不对 raise后面必须加一个异常类型 不能直接加东西
#test3() 报错

def test4(name):
    if name == 'dewei':
        raise Exception('dewei不可以被填写') #通用异常
    return name

#test4('dewei') 报错

#自定义异常类
class NumberLimitError(Exception): #自定义异常类型要继承Exception
    def __init__(self, message):
        self.message = message


class NameLimitError(Exception):
    def __init__(self, message):
        self.message = message


def test5(name):
    if name == 'dewei':
        raise NameLimitError('dewei不可以被填写') #NameLimitError是自定义异常类型
    return name

def test6(number):
    if number > 100:
        raise NumberLimitError('数字不可以大于100') #NumberLimitError是自定义异常类型
    return number

try:
    test5('dewei')
except NameLimitError as e: #捕获
    print(e)

try:
    test6(1000)
except NumberLimitError as e: #捕获
    print(e)


test5('dewei') #报错 错误类型就是NameLimitError