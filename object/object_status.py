# coding:utf-8
#此代码介绍了类的多态：保留子类中某个和父类名称一样的函数的功能
#2021-12-03

# 1 书写一个父类
class XiaomuFather(object):
    def talk(self):
        print('小慕的爸爸说了一句话')

    def dump(self):
        print('大家都可以跳')

# 2 书写一个子类，并且继承一个父类
class XiaomuBrother(XiaomuFather):
    def run(self):
        print('小慕哥哥在奔跑着..')

    def talk(self):
        print('小慕哥哥在说话...')

# 为什么要去多态
# 为什么要去继承父类
# 答案： 为了使用已经写好的类中的函数
# 为了保留子类中某个和父类名称一样的函数的功能，这时候，我们就用到了类的多态。
# ****可以帮助我们保留子类中的函数功能****

class Xiaomu(XiaomuFather):
    def talk(self):
        print('haha 小慕也可以开心的说自己的观点')


if __name__ == '__main__':
    xiaomu_brother = XiaomuBrother() #实例化
    xiaomu_brother.talk() #这里输出的是xiaomubrother的话而不是xiaomufather的话，尽管父子类都有talk函数，但是结果不同，这就是多态：保留子类中跟父类相同名称的函数多态
    xiaomu_brother.dump()
    print('____________________')
    father = XiaomuFather()  #实例化
    father.talk()
    print("___________________________")
    xiaomu = Xiaomu()  #实例化
    xiaomu.talk()
    xiaomu.dump()
