# coding:utf-8

#关于私有函数 私有变量
#2021-12-02

class Cat(object):
    __cat_type = 'meiduan' #私有属性

    def __init__(self, name, sex): #构造函数
        self.name = name
        self.__sex = sex #私有变量

    def run(self):
        result = self.__run()
        print(result)

    def __run(self): #私有函数
        return f'{self.__cat_type} type品种的小猫名字叫 {self.name} 性别是{self.__sex}， 开心的奔跑着'

    def dump(self):
        result = self.__dump()
        print(result)

    def __dump(self): #私有函数
        return f'{self.__cat_type} type品种的小猫名字叫 {self.name} 性别是{self.__sex} 开心的跳着'


class Test(object):
    pass #pass占位符防止报错


cat  = Cat(name='米粒儿', sex='boy') #实例化一下Cat类 （这就是实例化） 又称“创建一个Cat类的对象cat”
cat.run() #调用内置函数
cat.dump() #调用内置函数
#cat.__run()  #该语句报错 因为私有函数不能通过实例化对象调用

print("_______________________________________________________________")

print(dir(cat))  #用dir看一下cat里有哪些函数 变量 我们发现其中有个函数叫_Cat__dump,可以拿来调用私有函数
print(cat._Cat__dump()) #输出结果同上cat.dump()  #*调用的是私有函数，注意是函数()哦*

#print(cat.__sex) #该语句报错，因为不能调用私有属性
print(cat._Cat__sex) #不报错 返回值boy  #*调用的是私有变量，注意是变量哦*
print(cat._Cat__cat_type) #不报错 返回值meiduan #*调用的是私有变量，注意是变量哦*
