# coding:utf-8
# 多重继承：子类继承多个父类
# 2021-12-03

# 1 2个父类

class Tool(object):
    def work(self):
        return 'tool work'

    def car(self):
        return 'car will run'

class Food(object):
    def work(self):
        return 'food work'

    def cake(self):
        return 'i like cake'

# 继承父类的子类吧
class Person(Food, Tool): #具有相同名称函数时，最左边的类会先被继承，即food
    pass

if __name__ == '__main__':
    p = Person()
    p_car = p.car()
    p_cake = p.cake()
    print(p_car)
    print(p_cake)
    print("________________________")
    p_work = p.work()
    print(p_work) #打印的是food work而不是tool work：在最左边的类会先被继承，即food
    print("________________________")
    print(Person.__mro__) #__mro__会告诉我们person是如何继承的，他会打印继承顺序链
    #(<class '__main__.Person'>, <class '__main__.Food'>, <class '__main__.Tool'>, <class 'object'>)
    #先继承food然后是tool；object是这俩都继承的所以在后边
