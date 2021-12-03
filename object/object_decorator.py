# coding:utf-8

def check_str(func):
    print('func:', func)

    def inner(*args, **kwargs):
        print('args:', args, kwargs)
        result = func(*args, **kwargs)
        if result == 'ok':
            return 'result is %s' % result
        else:
            return 'result is failed:%s' % result

    return inner  # 回到外联函数的函数体中并return内联函数


@check_str
def test(data):
    return data


result = test('no') #元组 激活的是*args
print(result)

result = test(data='ok') #把变量名也带上了。 字典 激活的是*kwargs
print(result)
"""
func: <function test at 0x000002128F620E50>  #这里看出 外联函数连接到了test函数
args: ('no',) {}  #元组
result is failed:no
args: () {'data': 'ok'}  #字典
result is ok
"""