# coding:utf-8
#此代码介绍了类装饰器@classmethod @staticmethod  @property的用法
#2021-12-03

class Test(object):
    def __init__(self, a): #构造函数
        self.a = a

    def run(self):
        print('run')
        self.dump()  #2.但是可以在普通的self的类函数中调用带有classmethod、staticmethod的类函数
        self.sleep()

    @classmethod #作用：将类函数可以不经过实例化而直接被调用
    def dump(cls): #classmethod第一个参数须是cls
        print('dump')
        #cls.run()  #1.该语句报错，无法在classmethod装饰器的类函数中调用普通的self的类函数

    @staticmethod #作用：将类函数可以不经过实例化而直接被调用,被该装饰器调用的函数不许传递self或cls参数，且无法再该函数内调用其它类函数或类变量
    def sleep(): #没有参数
        print('i want sleep')

print("___________普通实例化操作_____________")
t = Test('a') #实例化-以往的普通操作
t.run()
print("___________classmethod操作________________")
Test.dump() #不实例化-@classmethod的效果：可以不通过实例化来调用类函数
print('-----------staticmethod操作-------------')
Test.sleep() #不实例化-@staticmethod的效果：可以不通过实例化来调用类函数
#t.sleep() #当然普通实例化也可以调用classmethod、staticmethod的类函数
# t.dump()
print("__________________下面是property用法________________________")



class Test1(object):
    def __init__(self, name):
        self.__name = name #这里定义的是私有变量，其实用普通变量x也可以，盲猜是为了和变量name作区分

    @property  #将类函数的执行免去括弧，类似于调用属性（变量）,只适用于无参数的类函数（self与cls除外）
    def name(self):
        return self.__name

    @name.setter #@property下设置属性值的装饰器 传参value（property的专用传参方式）
    def name(self, value):
        self.__name = value


t1 = Test1(name='dewei') #实例化
print(t1.name) #不用括弧就能打印哦，不过还是需要实例化一下
t1.name = '小慕' #setter用于传参
print(t1.name)



"""
关于@property不用括弧打印的解释
示例代码如下：
class AAA:
    def func(self):
        print('=============')

    @property
    def prop(self):
        return 100

aaa = AAA()
aaa.func()  # 调用实例方法
print(aaa.prop)  # 调用property属性

#=============
#180
"""

