# coding:utf-8

class Parent(object):
    def __init__(self, p):
        print('hello i am parent %s ' % p)


class Child(Parent):
    def __init__(self, c):
        super().__init__('parent') #super()保证了子类对于父类构造函数的继承
        print('hello i am child %s ' % c)


if __name__ == '__main__':
    x = Child(c='Child')
"""
hello i am parent parent 
hello i am child Child 
"""