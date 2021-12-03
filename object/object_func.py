# coding:utf-8
# 介绍类中的几个常用函数：__str__;__getattr__;__setattr__;__call__ (都是类的内置函数所以两边都有下划线)
# 2021-12-03

class Test(object):

    def __str__(self): #如果定义了该函数，当print当前实例化对象的时候，会返回该函数的return信息
        return 'this is a test class'

    def __getattr__(self, key):  #当调用的属性或者方法不存在 时，会返回该方法定义的信息 (key可以随便写)
        return '这个key:{}并不存在'.format(key)

    def __setattr__(self, key, value): #拦截当前类中不存在的属性与值 #这里不太懂
        self.__dict__[key] = value
        print(self.__dict__)

    def __call__(self, a): #本质是将一个类变成一个函数 “使得实例对象变为可调用对象（像普通函数一样）”
        print('call func will start')
        print(a)

t = Test() #类的实例化
print("________str___________")
print(t) #print实例化对象，__str__函数发挥作用
print("________getattr___________")
print(t.a) #调用的属性或方法不存在
print(t.b) #调用的属性或方法不存在
print("__________________setattr___________________")
t.name = 'test'    #输出:{'name': 'test'}
print(t.name)      #输出:test
print("__________________call________________________")
t('dewei')#因为t已经实例化过了，所以调用__call__直接对传入的值进行操作
"""输出：
call func will start
dewei
"""

#t.a.b.c 链式操作 #报错，不能用实例化对象直接调用多个属性 下面的例子解决此问题：实现链式属性操作

print("____________________链式属性操作(多个点.)_________________________")

class Test2(object):
    def __init__(self, attr=''):
        self.__attr = attr

    def __call__(self, name):
        return name

    def __getattr__(self, key): #属性不存在的时候就会调用getattr
        if self.__attr: #如果存在
            key = '{}.{}'.format(self.__attr, key)
        else: #如果不存在
            key = key
        print(key)
        return Test2(key) #类函数调用类对象，通过括弧完成了实例化   ？什么意思

t2 = Test2()
name = t2.a.b.c('dewei')

print(name)

print("___________________")

result = t2.name.age.sex('ok')
print(result)

"""
_setattr__()在属性赋值时被调用，并且将值存储到实例字典中，
这个字典应该是self的__dict__属性。即：在类实例的每个属性进行赋值时，
都会首先调用__setattr__()方法，并在__setattr__()方法中将属性名和属性值添加到类实例的__dict__属性中。
"""