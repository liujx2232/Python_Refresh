# coding:utf-8

from animal import dog_run
from animal import cat_run
from animal.cat.action import cat_name
# from animal.cat.action import Cat #类的导入
#
# cat = Cat() #类的实例化
# cat.run() #类实例化后的调用

dog_run_result = dog_run() #在animal包的_init_中定义过
cat_run_result = cat_run()

print(dog_run_result)
print(cat_run_result)
print(cat_name) #在animal包的cat包的action模块里
