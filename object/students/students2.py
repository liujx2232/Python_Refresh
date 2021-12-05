# coding:utf-8

'''
   学生信息库 通过原学生信息库代码引入类的修改
   2021-12-04
'''

class StudentInfo(object):
    def __init__(self, students):
        self.students = students

    def get_by_id(self, student_id):
        return self.students.get(student_id)

    def get_all_students(self): #修改时要把students参数全变成self.students
        for id_, value in self.students.items(): #id是个关键字所以加了下划线以区分
            print('学号：{}, 姓名:{}, 年龄:{}, 性别:{}, 班级:{}'.format(
                id_, value['name'], value['age'], value['sex'], value['class_number']
            ))
        return self.students

    def add(self, **student):
        check = self.check_user_info(**student)
        if check != True:
            print(check)
            return
        self.__add(**student)

    def adds(self, new_students):  #新的：批量功能添加函数
        for student in new_students:
            check = self.check_user_info(**student) #验证传入的成员是否合法
            if check != True:
                print(check, student.get('name'))
                continue
            self.__add(**student) #这里原来写的是用add函数做，但是add又会调用一遍check_user_info函数，这样adds函数调用了两遍这个，造成冗余，所以我们写了私有函数__add

    def __add(self, **student): #该函数作用：用于adds函数中替换add函数，防止进行两遍check_user_info
        new_id = max(self.students) + 1
        self.students[new_id] = student

    def delete(self, student_id):
        if student_id not in self.students:
            print('{} 并不存在'.format(student_id))
        else:
            user_info = self.students.pop(student_id)
            print('学号是{}, {}同学的信息已经被删除了'.format(student_id, user_info['name']))

    def deletes(self, ids):
        for id_ in ids:
            if id_ not in self.students:
                print(f'{id_} 不存在学生库中')
                continue
            student_info = self.students.pop(id_)
            print(f'学号{id_} 学生{student_info["name"]} 已被移除')

    def update(self, student_id, **kwargs):
        if student_id not in self.students:
            print('并不存在这个学号:{}'.format(student_id))

        check = self.check_user_info(**kwargs)
        if check != True:
            print(check)
            return

        self.students[student_id] = kwargs
        print('同学信息更新完毕')

    def updates(self, update_students):
        for student in update_students:
            id_ = list(student.keys())[0]
            if id_ not in self.students:
                print(f'学号{id_} 不存在')
                continue
            user_info = student[id_]
            check = self.check_user_info(**user_info)
            if check != True:
                print(check)
                continue
            self.students[id_] = user_info
        print('所有用户信息更新完成')

    def search_users(self, **kwargs):
        values = list(self.students.values()) #因为姓名年龄班级可能有相同的同学所以需要使用列表类型
        key = None
        value = None
        result = []

        if 'name' in kwargs:
            key = 'name'
            value = kwargs[key]
        elif 'sex' in kwargs:
            key = 'sex'
            value = kwargs['sex']
        elif 'class_number' in kwargs:
            key = 'class_number'
            value = kwargs[key]
        elif 'age' in kwargs:
            key = 'age'
            value = kwargs[key]
        else:
            print('没有发现搜索的关键字')
            return

        for user in values:  # [{name, sex, age, class_number}, {}]
            if value in user[key]:  #这里升级了模糊查找功能，原语句:if user[key] == value:
                result.append(user)
        return result

    def check_user_info(self, **kwargs):
        if 'name' not in kwargs:
            return '没有发现学生姓名'
        if 'age' not in kwargs:
            return '缺少学生年龄'
        if 'sex' not in kwargs:
            return '缺少学生性别'
        if 'class_number' not in kwargs:
            return '缺少学生班级'
        return True

students = {
    1: {
        'name': 'dewei',
        'age': 33,
        'class_number': 'A',
        'sex': 'boy'
    },
    2: {
        'name': '小慕',
        'age': 10,
        'class_number': 'B',
        'sex': 'boy'
    },
    3: {
        'name': '小曼',
        'age': 18,
        'class_number': 'A',
        'sex': 'girl'
    },
    4: {
        'name': '小高',
        'age': 18,
        'class_number': 'C',
        'sex': 'boy'
    },
    5: {
        'name': '小云',
        'age': 18,
        'class_number': 'B',
        'sex': 'girl'
    }
} #在字典中存储了五个字典


if __name__ == '__main__':
    print("____________________根据序号查询学生信息_________________________")
    student_info = StudentInfo(students) #类实例化并传入students
    user = student_info.get_by_id(1)
    print(user)  #{'name': 'dewei', 'age': 33, 'class_number': 'A', 'sex': 'boy'}
    print("___________________通过add添加一个学生信息__________________________")
    student_info.add(name='dewei2', age=344, class_number='A', sex='boy')
    student_info.get_all_students()
    print("___________________通过adds批量添加多个学生信息_________________________")
    users = [
        {'name': 'xiaoming', 'age': 17, 'class_number': 'B', 'sex': 'boy'},
        {'name': 'xiaohong', 'age': 18, 'class_number': 'C', 'sex': 'girl'}
    ] #列表
    student_info.adds(users)
    student_info.get_all_students()
    print('---------------------通过deletes批量删除-------------------------')
    student_info.deletes([7, 8])
    student_info.get_all_students()
    print('---------------------通过updates批量更新------------------------')
    student_info.updates([
        {1: {'name': 'dewei.zhang', 'age': 18, 'class_number': 'A', 'sex': 'boy'}},
        {2: {'name': '小慕同学', 'age': 18, 'class_number': 'A', 'sex': 'boy'}}
    ])
    student_info.get_all_students()
    print("--------------------通过search_users模糊查找查找学生------------------------------")
    result = student_info.search_users(name='d')
    print(result)
    result = student_info.search_users(name='小')
    print(result)
    print('------')
    result = student_info.search_users(name='')
    print(result)
    result = student_info.search_users(name='小')
    print(result)
    print('-----')
    result = student_info.search_users(name='') #空字符串会查找到所有人
    print(result)
