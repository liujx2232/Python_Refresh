# coding:utf-8

import os
import os.path

current_path = os.getcwd()
print("1",current_path) #返回当前的路径
print("2",os.path.isabs(current_path)) #是否是绝对路径：True
print("3",os.path.isabs('animal'))  #是否是绝对路径：False



new_path = '%s/test1' % current_path #在当前路径下建立test1新文件夹
if os.path.exists(new_path):
    os.makedirs(new_path) #创建多级文件夹函数

data = os.listdir(current_path) #返回指定路径下所有的文件和文件夹
print("4",data)

new_path2 = os.path.join(current_path, 'test2', 'abc') #路径字符串合并 创建test2文件夹并在里面创建abc
print("5",new_path2)
if os.path.exists(new_path2): #os.path模块返回布尔类型，其中中exist函数：查看文件和路径是否存在
    os.makedirs(new_path2)
if os.path.exists('test3'):
    os.makedirs('test3')

if os.path.exists('test2/abc'):
    os.removedirs('test2/abc') #删除多级文件夹 删除test2下的abc
if os.path.exists('test3'):
    os.rename('test3', 'test3_new') #改名函数
if os.path.exists('pip_image.py'):
    os.rename('pip_image.py', 'pip3_image.py')
if os.path.exists('%s/test3_new' % current_path):
    os.rmdir('%s/test3_new' % current_path)
if os.path.exists('test1'):
    os.rmdir('test1')

current_path = current_path + '/package_os.py'
print("6",os.path.isfile(current_path)) #是否是文件
print("7",os.path.split(current_path)) #以最后一层路径为基准切割
print("8",os.path.isdir(os.path.split(current_path)[0])) #isdir判断是否是路径 （零索引是路径）

print("9",dir(os.path))
